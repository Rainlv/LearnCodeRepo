using System;
using System.Windows.Forms;

using ESRI.ArcGIS.Carto;
using ESRI.ArcGIS.Geometry;
using ESRI.ArcGIS.Geoprocessor;
using ESRI.ArcGIS.Controls;

namespace Statistics
{
    public partial class FormBuffer : Form
    {
        private AxMapControl cur_map;
        private string outShpFilePath;
        private IFeatureLayer currentLayer;

        public IFeatureLayer CurrentLayer
        {
            get { return currentLayer; }
            set { currentLayer = value; }
        }

        public string OutShpFilePath
        {
            get { return outShpFilePath; }
            set { outShpFilePath = value; }
        }

        public AxMapControl Current_map
        {
            get { return cur_map; }
            set { cur_map = value; }
        }

        public FormBuffer()
        {
            InitializeComponent();
        }

        public FormBuffer(AxMapControl c_map)
            : this()
        {
            Current_map = c_map;
        }

        private void FormQueryBySpatial_Load(object sender, EventArgs e)
        {
            comboBoxLayerName.Items.Clear();

            # region combobox添加图层名
            for (int i = 0; i < Current_map.LayerCount; i++)
            {
                if (Current_map.get_Layer(i) is GroupLayer)
                {
                    ICompositeLayer subLayer = Current_map.get_Layer(i) as ICompositeLayer;
                    for (int j = 0; j < subLayer.Count; j++)
                    {
                        comboBoxLayerName.Items.Add(subLayer.get_Layer(i).Name);
                    }
                }  // endif
                else
                {
                    comboBoxLayerName.Items.Add(Current_map.get_Layer(i).Name);
                }
            }
            # endregion

            try
            {
                comboBoxLayerName.SelectedIndex = 0;
            }
            catch (System.Exception)
            { Console.WriteLine("添加图层名 error occur"); }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            SaveFileDialog buffer_filePath = new SaveFileDialog();

            buffer_filePath.Title = "保存Shp文件";
            buffer_filePath.Filter = "ShpFile(*.shp)|*.shp";

            buffer_filePath.ShowDialog();


            OutShpFilePath = buffer_filePath.FileName;
            textBoxoutFilePath.Text = OutShpFilePath;
        }

        private void buttonApply_Click(object sender, EventArgs e)
        {
            bufferAnalyze();
        }

        private void comboBoxLayerName_SelectedIndexChanged(object sender, EventArgs e)
        {
            # region 获得选中图层
            for (int i = 0; i < Current_map.LayerCount; i++)
            {
                if (Current_map.get_Layer(i) is GroupLayer)
                {
                    ICompositeLayer subLayer = Current_map.get_Layer(i) as ICompositeLayer;
                    for (int j = 0; j < subLayer.Count; j++)
                    {
                        if (subLayer.get_Layer(i).Name == comboBoxLayerName.SelectedItem.ToString())
                        {
                            CurrentLayer = subLayer.get_Layer(i) as IFeatureLayer;
                            break;
                        }
                    }
                }
                else
                {
                    if (Current_map.get_Layer(i).Name == comboBoxLayerName.SelectedItem.ToString())
                    {
                        CurrentLayer = Current_map.get_Layer(i) as IFeatureLayer;
                    }
                }

            }
            # endregion
        }

        private void buttonOK_Click(object sender, EventArgs e)
        {
            bufferAnalyze();
            this.Close();
        }

        private void bufferAnalyze()
        {
            Geoprocessor gp = new Geoprocessor();
            gp.OverwriteOutput = true;
            ESRI.ArcGIS.AnalysisTools.Buffer pBuffer = new ESRI.ArcGIS.AnalysisTools.Buffer();

            pBuffer.in_features = CurrentLayer;


            pBuffer.out_feature_class = OutShpFilePath;

            pBuffer.buffer_distance_or_field = textBoxBufferDistance.Text + " Meters";
            pBuffer.dissolve_option = "All";

            gp.Execute(pBuffer, null);

            string outDir = System.IO.Path.GetDirectoryName(OutShpFilePath);
            string filename = System.IO.Path.GetFileName(OutShpFilePath);
            Current_map.AddShapeFile(outDir, filename);
            Current_map.MoveLayerTo(1, 0);
        }

        private void buttonClose_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
        
}
