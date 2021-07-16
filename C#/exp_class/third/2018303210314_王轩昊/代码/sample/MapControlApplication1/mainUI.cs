using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using ESRI.ArcGIS.esriSystem;
using ESRI.ArcGIS.Carto;
using ESRI.ArcGIS.Controls;
using ESRI.ArcGIS.ADF;
using ESRI.ArcGIS.SystemUI;
using ESRI.ArcGIS.Geometry;
using ESRI.ArcGIS.DataSourcesFile;
using ESRI.ArcGIS.DataSourcesGDB;
using ESRI.ArcGIS.DataSourcesRaster;
using ESRI.ArcGIS.Geodatabase;
using ESRI.ArcGIS.ADF.BaseClasses;

namespace MapControlApplication1
{
    public partial class mainUI : Form
    {
        public mainUI()
        {
            InitializeComponent();
        }

        private void openMapToolStripMenuItem_Click(object sender, EventArgs e)
        {
            openFileDialog1.Filter = "Mxd文件(*.mxd)|*.mxd";
            openFileDialog1.Title = "打开mxd文件";
            if (openFileDialog1.ShowDialog() == System.Windows.Forms.DialogResult.OK)
            {
                string path = openFileDialog1.FileName;
                IMapControl2 curMap = this.axMapControl1.Object as IMapControl2;
                curMap.LoadMxFile(path);
            }
        }

        private void exitToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void zoomOutToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void toolsToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        int tools_id;

        private void zoomToolStripMenuItem_Click(object sender, EventArgs e)
        {
            tools_id = 1;
        }

        private void zoomByRectToolStripMenuItem_Click(object sender, EventArgs e)
        {
            tools_id = 2;
        }

        private void fullScreenToolStripMenuItem_Click(object sender, EventArgs e)
        {
            axMapControl1.Extent = axMapControl1.FullExtent;
        }

        private void axMapControl1_OnMouseDown(object sender, IMapControlEvents2_OnMouseDownEvent e)
        {
            axMapControl1.Pan();
            switch (this.tools_id)
            {
                case 1:
                    IMapControlDefault ctrl_map1 = this.axMapControl1.Object as IMapControlDefault;
                    IGeometry draw_circle1 = ctrl_map1.TrackCircle();
                    ctrl_map1.Extent = draw_circle1.Envelope;
                    ctrl_map1.ActiveView.PartialRefresh(esriViewDrawPhase.esriViewAll, null, null);
                    break;
                case 2:
                    IMapControlDefault ctrl_map2 = this.axMapControl1.Object as IMapControlDefault;
                    IGeometry draw_rect2 = ctrl_map2.TrackRectangle();
                    ctrl_map2.Extent = draw_rect2.Envelope;
                    ctrl_map2.ActiveView.PartialRefresh(esriViewDrawPhase.esriViewAll, null, null);
                    break;
                case 3:
                    break;
                default:
                    break;
            }
        }

        private void panToolStripMenuItem_Click(object sender, EventArgs e)
        {
            tools_id = 3;
        }

        // 加载shpfile
        private void openShpToolStripMenuItem_Click(object sender, EventArgs e)
        {
            OpenFileDialog pOpenFileDialog = new OpenFileDialog();
            pOpenFileDialog.CheckFileExists = true;
            pOpenFileDialog.Title = "打开shape文件";
            pOpenFileDialog.Filter = "Shape文件(*.shp)|*.shp";
            pOpenFileDialog.ShowDialog();

            string pPullPath = pOpenFileDialog.FileName;
            if (String.IsNullOrEmpty(pPullPath)) return;
            int pIndex = pPullPath.LastIndexOf("\\");
            string pFilePath = pPullPath.Substring(0, pIndex);
            string pFileName = pPullPath.Substring(pIndex + 1);


            // 使用工作空间加载
            IWorkspaceFactory pWorkspaceFactor = new ShapefileWorkspaceFactory();
            IFeatureWorkspace pFeatureWorkspace = (IFeatureWorkspace)pWorkspaceFactor.OpenFromFile(pFilePath, 0);
            IFeatureClass pFeatureClass = pFeatureWorkspace.OpenFeatureClass(pFileName);
            IFeatureLayer pFeatureLayer = new FeatureLayer();
            pFeatureLayer.FeatureClass = pFeatureClass;
            pFeatureLayer.Name = pFeatureLayer.FeatureClass.AliasName;
            axMapControl1.Map.AddLayer(pFeatureLayer);

            // 使用接口加载
            //string pFileNameWithoutExtension = pFileName.Substring(0, pFileName.LastIndexOf("."));
            //axMapControl1.AddShapeFile(pFilePath, pFileNameWithoutExtension);

            axMapControl1.ActiveView.Refresh();

        }

        private void openMapToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            openMapToolStripMenuItem_Click(sender, e);
        }

        private void openShpToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            openShpToolStripMenuItem_Click(sender, e);
        }

        // 加载栅格
        private void openRasterToolStripMenuItem_Click(object sender, EventArgs e)
        {
            OpenFileDialog pOpenFileDialog = new OpenFileDialog();
            pOpenFileDialog.CheckFileExists = true;
            pOpenFileDialog.Title = "打开Raster文件";
            pOpenFileDialog.Filter = "栅格文件(*.*)|*.bmp;*.tif;*.jpg;*.img;|(*.bmp)|*.bmp|(*.tif)|*.tif|(*.jpg)|*.jpg|(*.img)|*.img";
            pOpenFileDialog.ShowDialog();

            string pRasFileName = pOpenFileDialog.FileName;
            if (String.IsNullOrEmpty(pRasFileName)) return;

            string pPath = System.IO.Path.GetDirectoryName(pRasFileName);
            string pFileName = System.IO.Path.GetFileName(pRasFileName);

            IWorkspaceFactory pWorkspaceFactory = new RasterWorkspaceFactory();
            IWorkspace pWorksapce = pWorkspaceFactory.OpenFromFile(pPath, 0);
            IRasterWorkspace pRasterWorkspace = pWorksapce as IRasterWorkspace;
            IRasterDataset pRasterDataset = pRasterWorkspace.OpenRasterDataset(pFileName);

            IRasterPyramid3 pRasPyrmid = pRasterDataset as IRasterPyramid3;

            if (pRasPyrmid != null)
            {
                pRasPyrmid.Create();
            }

            IRaster pRaster = pRasterDataset.CreateDefaultRaster();
            IRasterLayer pRasterLayer = new RasterLayerClass();
            pRasterLayer.CreateFromRaster(pRaster);
            ILayer pLayer = pRasterLayer as ILayer;
            axMapControl1.AddLayer(pLayer, 0);

            axMapControl1.ActiveView.Refresh();

        }

        private void toolStripMenuItem2_Click(object sender, EventArgs e)
        {

        }


        ILayer pMoveLayer;
        int toIndex;
        ESRI.ArcGIS.Geometry.Point pMoveLayerPoint = new ESRI.ArcGIS.Geometry.Point();

        private void axTOCControl1_OnMouseDown(object sender, ITOCControlEvents_OnMouseDownEvent e)
        {

            esriTOCControlItem pItem = esriTOCControlItem.esriTOCControlItemNone;
            IBasicMap pMap = null;
            object unk = null;
            object data = null;
            ILayer pLayer = null;
            axTOCControl1.HitTest(e.x, e.y, ref pItem, ref pMap, ref pLayer, ref unk, ref data);

            # region 弹出右键菜单
            IFeatureLayer pTocFeatureLayer = pLayer as IFeatureLayer;

            if (e.button == 2)
            {
                if (pItem == esriTOCControlItem.esriTOCControlItemLayer && pTocFeatureLayer != null)
                {
                    contextMenuStrip1.Show(Control.MousePosition);
                }
            }
            # endregion


            if (e.button == 1)
            {
                pMoveLayerPoint.PutCoords(e.x, e.y);

                if (pItem == esriTOCControlItem.esriTOCControlItemLayer)
                {
                    if (pLayer is IAnnotationLayer) return;
                    else pMoveLayer = pLayer;
                }

            }
            
        }


        private void axTOCControl1_OnMouseUp(object sender, ITOCControlEvents_OnMouseUpEvent e)
        {
            try
            {
                if (e.button == 1 && pMoveLayer != null && pMoveLayerPoint.Y != e.y)
                {
                    esriTOCControlItem pItem = esriTOCControlItem.esriTOCControlItemNone;
                    IBasicMap pBasicMap = null;
                    object unk = null;
                    object data = null;
                    ILayer pLayer = null;
                    axTOCControl1.HitTest(e.x, e.y, ref pItem, ref pBasicMap, ref pLayer, ref unk, ref data);

                    IMap pMap = axMapControl1.ActiveView.FocusMap;
                    if (pLayer!=null || pItem == esriTOCControlItem.esriTOCControlItemLayer)
                    {
                        if (pMoveLayer != pLayer)
                        {
                            ILayer pTempLayer;
                            for (int i = 0; i < pMap.LayerCount; i++)
                            {
                                pTempLayer = pMap.get_Layer(i);
                                if (pTempLayer == pLayer)
                                {
                                    toIndex = i;
                                }
                            }
                        }

                    }
                    else if (pItem == esriTOCControlItem.esriTOCControlItemMap)
                    {
                        toIndex = 0;
                    }
                    else if (pItem == esriTOCControlItem.esriTOCControlItemNone)
                    {
                        toIndex = pMap.LayerCount - 1;
                    }
                    pMap.MoveLayer(pMoveLayer, toIndex);
                    axMapControl1.ActiveView.Refresh();
                    axTOCControl1.Update();
                }

            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }


    }
}
