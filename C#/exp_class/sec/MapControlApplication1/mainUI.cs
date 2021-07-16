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
            tools_id = 1; // 圆形缩放
        }

        private void zoomByRectToolStripMenuItem_Click(object sender, EventArgs e)
        {
            tools_id = 2; // 矩形缩放
        }

        private void fullScreenToolStripMenuItem_Click(object sender, EventArgs e)
        {
            axMapControl1.Extent = axMapControl1.FullExtent; // 全图展示
        }

        // 缩放
        private void axMapControl1_OnMouseDown(object sender, IMapControlEvents2_OnMouseDownEvent e)
        {
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
                    axMapControl1.Pan();
                    break;
                default:
                    break;
            }
        }

        private void panToolStripMenuItem_Click(object sender, EventArgs e)
        {
            tools_id = 3;  // 移动图层展示区域（Pan）
        }

    }
}