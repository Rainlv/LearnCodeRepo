using System;
using System.Windows.Forms;
using ESRI.ArcGIS.Carto;
using ESRI.ArcGIS.Controls;
using MapControlApplication1.Tools.FileOpener;
using MapControlApplication1.Tools.Zoom;
using System.Collections;
using MapControlApplication1.Tools;
using MapControlApplication1.Tools.Select;

namespace MapControlApplication1
{
    public partial class mainUI : Form
    {
        ArrayList zoomBtns = new ArrayList();
        ArrayList FC_selectBtns = new ArrayList();
        public mainUI()
        {
            InitializeComponent();
            zoomBtns.Add(zoomByCircleToolStripMenuItem);
            zoomBtns.Add(zoomByRectToolStripMenuItem);
            zoomBtns.Add(panToolStripMenuItem);
            FC_selectBtns.Add(byPointToolStripMenuItem);
            FC_selectBtns.Add(byRectToolStripMenuItem);
            FC_selectBtns.Add(byLineToolStripMenuItem);
        }

        // Circle
        private void zoomToolStripMenuItem_Click(object sender, EventArgs e)
        {
            axMapControl1.CurrentTool = null; 
            if (zoomByCircleToolStripMenuItem.Checked)
            {
                this.button_check(zoomBtns,zoomByCircleToolStripMenuItem);
                Circle zoomTool = new Circle();
                zoomTool.OnCreate(this.axMapControl1.Object);
                axMapControl1.CurrentTool = zoomTool;
                
            }
        }

        // Rect
        private void zoomByRectToolStripMenuItem_Click(object sender, EventArgs e)
        {
            axMapControl1.CurrentTool = null;
            if (zoomByRectToolStripMenuItem.Checked)
            {
                this.button_check(zoomBtns, zoomByRectToolStripMenuItem);
                Rect zoomTool = new Rect();
                zoomTool.OnCreate(this.axMapControl1.Object);
                axMapControl1.CurrentTool = zoomTool;
            }
        }

        // fullScreen
        private void fullScreenToolStripMenuItem_Click(object sender, EventArgs e)
        {
            axMapControl1.Extent = axMapControl1.FullExtent;
        }

        // Pan
        private void panToolStripMenuItem_Click(object sender, EventArgs e)
        {
            axMapControl1.CurrentTool = null;
            if (panToolStripMenuItem.Checked)
            {
                this.button_check(zoomBtns, panToolStripMenuItem);
                Pan zoomTool = new Pan();
                zoomTool.OnCreate(this.axMapControl1.Object);
                axMapControl1.CurrentTool = zoomTool;
            }
        }

        // 加载Mxd
        private void openMapToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            MapOpener zoomTool = new MapOpener();
            zoomTool.OnCreate(this.axMapControl1.Object);
            axMapControl1.CurrentTool = zoomTool;
        }

        // 加载Shp
        private void openShpToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            ShpOpener zoomTool = new ShpOpener();
            zoomTool.OnCreate(this.axMapControl1.Object);
            axMapControl1.CurrentTool = zoomTool;
        }

        // 加载栅格
        private void openRasterToolStripMenuItem_Click(object sender, EventArgs e)
        {
            RasOpener zoomTool = new RasOpener();
            zoomTool.OnCreate(this.axMapControl1.Object);
            axMapControl1.CurrentTool = zoomTool;
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
        
        private void button_check(ArrayList btns, ToolStripMenuItem ck_btn)
        {
            foreach (ToolStripMenuItem btn in btns)
            {
                if (btn!=ck_btn)
                {
                    btn.Checked = false;
                }
            }
        }

        private void byPointToolStripMenuItem_MouseDown(object sender, MouseEventArgs e)
        {
            axMapControl1.CurrentTool = null;
            if (!byPointToolStripMenuItem.Checked) // 这里取反是因为链接的是鼠标按下事件而不是点击事件，勾选是鼠标弹起后才勾上的
            {
                button_check(FC_selectBtns, byPointToolStripMenuItem);
                byPoint zoomTool = new byPoint();
                zoomTool.OnCreate(this.axMapControl1.Object);
                axMapControl1.CurrentTool = zoomTool;
            }

        }

        private void byRectToolStripMenuItem_Click(object sender, EventArgs e)
        {
            axMapControl1.CurrentTool = null;
            if (byRectToolStripMenuItem.Checked)
            {
                button_check(FC_selectBtns, byRectToolStripMenuItem);
                byRect zoomTool = new byRect();
                zoomTool.OnCreate(this.axMapControl1.Object);
                axMapControl1.CurrentTool = zoomTool;
            }
        }

        private void byLineToolStripMenuItem_Click(object sender, EventArgs e)
        {
            axMapControl1.CurrentTool = null;
            if (byLineToolStripMenuItem.Checked)
            {
                button_check(FC_selectBtns, byLineToolStripMenuItem);
                byLine zoomTool = new byLine();
                zoomTool.OnCreate(this.axMapControl1.Object);
                axMapControl1.CurrentTool = zoomTool;
            }
        }
    }
}
