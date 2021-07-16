using System;
using System.Windows.Forms;

using ESRI.ArcGIS.Carto;
using ESRI.ArcGIS.Geodatabase;

namespace Query
{
    public partial class FormQueryByAttribute : Form
    {
        private IMap current_map;
        private IFeatureLayer current_layer;
        private string current_field;

        public string Current_field
        {
            get { return current_field; }
            set { current_field = value; }
        }

        public IFeatureLayer Current_layer
        {
            get { return current_layer; }
            set { current_layer = value; }
        }

        public IMap Current_map
        {
          get { return current_map; }
          set { current_map = value; }
        }

        private FormQueryByAttribute()
        {
            InitializeComponent();
        }

        public FormQueryByAttribute(IMap c_map):this()
        {
            Current_map = c_map;
        }


        // combobox添加图层名
        private void FormQueryByAttribute_Load(object sender, EventArgs e)
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
                comboBoxSelectMethod.SelectedIndex = 0;

            }
            catch (System.Exception)
            { Console.WriteLine("添加图层名 error occur"); }

        }

        // 添加图层字段
        private void comboBoxLayerName_SelectedIndexChanged(object sender, System.EventArgs e)
        {
            listBoxFields.Items.Clear();
            listBoxValues.Items.Clear();
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
                            Current_layer = subLayer.get_Layer(i) as IFeatureLayer;
                            break;
                        }
                    }
                }
                else
                {
                    if (Current_map.get_Layer(i).Name == comboBoxLayerName.SelectedItem.ToString())
                    {
                        Current_layer = Current_map.get_Layer(i) as IFeatureLayer;
                    }
                }

            }
            # endregion

            // 添加字段名称
            for (int i = 0; i < Current_layer.FeatureClass.Fields.FieldCount; i++)
            {
                IField field = Current_layer.FeatureClass.Fields.get_Field(i);
                if (field.Name.ToUpper() != "SHAPE")
                {
                    listBoxFields.Items.Add(field.Name);
                }
            }
        }

        // 获取唯一值
        private void buttonGetUniqeValue_Click(object sender, System.EventArgs e)
        {
            listBoxValues.Items.Clear();
            IDataset dataSet = Current_layer.FeatureClass as IDataset;
            IQueryDef query = ((IFeatureWorkspace)dataSet.Workspace).CreateQueryDef();
            query.Tables = dataSet.Name;
            query.SubFields = "DISTINCT(" + Current_field + ")";
            ICursor cursor = query.Evaluate();
            IRow row = cursor.NextRow();

            IFields fields = Current_layer.FeatureClass.Fields;
            IField field = fields.get_Field(fields.FindField(Current_field));

            while (row != null)
            {
                if (field.Type == esriFieldType.esriFieldTypeString)
                {
                    listBoxValues.Items.Add("'" + row.get_Value(0).ToString() + "'");
                }
                else
                {
                    listBoxValues.Items.Add(row.get_Value(0).ToString());
                }
                
                row = cursor.NextRow();
            }
        }

        // 获得选中字段名
        private void listBoxFields_SelectedIndexChanged(object sender, System.EventArgs e)
        {
            Current_field = listBoxFields.SelectedItem.ToString();
        }

        // 双击字段加到where语句
        private void listBoxFields_DoubleClick(object sender, System.EventArgs e)
        {
            textBoxWhere.Text += "\"" + listBoxFields.SelectedItem.ToString() + "\"";
        }

        // 双击按钮加到where
        private void buttonEqual_Click(object sender, System.EventArgs e)
        {
            textBoxWhere.Text += " " + ((Button)sender).Text + " ";
        }

        // 双击唯一值加到where
        private void listBoxValues_DoubleClick(object sender, System.EventArgs e)
        {
            try
            {
                textBoxWhere.Text += listBoxValues.SelectedItem.ToString();
            }
            catch (Exception)
            {
                
            }
            
        }

        // 清除where
        private void buttonClear_Click(object sender, System.EventArgs e)
        {
            textBoxWhere.Clear();
        }

        private void SelectFeatureByAttr()
        {
            IFeatureSelection F_selector = Current_layer as IFeatureSelection;
            IQueryFilter queryFilter = new QueryFilterClass();
            queryFilter.WhereClause = textBoxWhere.Text;
            IActiveView activeView = Current_map as IActiveView;
            switch (comboBoxSelectMethod.SelectedIndex)
            {
                case 0:
                    Current_map.ClearSelection();
                    F_selector.SelectFeatures(queryFilter, esriSelectionResultEnum.esriSelectionResultNew, false);
                    break;
                case 1:
                    F_selector.SelectFeatures(queryFilter, esriSelectionResultEnum.esriSelectionResultAdd, false);
                    break;
                case 2:
                    F_selector.SelectFeatures(queryFilter, esriSelectionResultEnum.esriSelectionResultXOR, false);
                    break;
                case 3:
                    F_selector.SelectFeatures(queryFilter, esriSelectionResultEnum.esriSelectionResultAnd, false);
                    break;
                default:
                    Current_map.ClearSelection();
                    F_selector.SelectFeatures(queryFilter, esriSelectionResultEnum.esriSelectionResultNew, false);
                    break;
            }
            activeView.PartialRefresh(esriViewDrawPhase.esriViewGeoSelection, null, activeView.Extent);
        }

        // 确定按钮
        private void buttonOK_Click(object sender, System.EventArgs e)
        {
            try
            {
                SelectFeatureByAttr();
            }
            catch (System.Exception)
            {
                Console.WriteLine("buttonOK_Click error occur");
                MessageBox.Show("无效的查询语句");
            }


            this.Close();
        }

        // 应用按钮
        private void buttonApply_Click(object sender, System.EventArgs e)
        {
            //try
            //{
                //SelectFeatureByAttr();
                //ShowAttributes();
            //}
            //catch (System.Exception)
            //{
            //    Console.WriteLine("buttonApply_Click error occur");
            //    MessageBox.Show("无效的查询语句");
            //}

            SelectFeatureByAttr();
            ShowAttributes();


            textBoxWhere.SelectAll();
            textBoxWhere.Focus();
        }

        private void buttonClose_Click(object sender, System.EventArgs e)
        {
            this.Close();
        }

        void ShowAttributes()
        {
            //首先清空DataGridView中的行和列
            dataGridView.DataSource = null;
            dataGridView.Columns.Clear();
            dataGridView.Rows.Clear();


            //通过接口转换，使用IFeatureSelection接口获取图层的选择集
            IFeatureSelection featureSelection = Current_layer as IFeatureSelection;
            //通过ISelectionSet接口获取被选择的要素集合
            ISelectionSet selectionSet = featureSelection.SelectionSet;
            //通过ISelectionSet接口的Count属性可以获取被选择要素的数量
            labelLayerSelectionCount.Text = "当前图层选择了 " + selectionSet.Count + " 个要素。";

            //对当前图层要素的属性字段进行遍历，从而建立DataGridView中的列
            //获取所有的属性字段
            IFields fields = Current_layer.FeatureClass.Fields;
            for (int i = 0; i < fields.FieldCount; i++)
            {
                //通过遍历添加列，使用字段的AliasName作为DataGridView中显示的列名
                dataGridView.Columns.Add(fields.get_Field(i).Name, fields.get_Field(i).AliasName);
            }

            //对选择集进行遍历，从而建立DataGridView中的行
            //定义ICursor接口的游标以遍历整个选择集
            ICursor cursor;
            //使用ISelectionSet接口的Search方法，使用null作为查询过滤器，cursor作为返回值获取整个选择集
            selectionSet.Search(null, false, out cursor);
            //进行接口转换，使用IFeatureCursor接口来获取选择集中的每个要素
            IFeatureCursor featureCursor = cursor as IFeatureCursor;
            //获取IFeature接口的游标中的第一个元素
            IFeature feature = featureCursor.NextFeature();
            //定义string类型的数组，以添加DataGridView中每一行的数据
            string[] strs;
            //当游标不为空时
            while (feature != null)
            {
                //string数组的大小为字段的个数
                strs = new string[fields.FieldCount];
                //对字段进行遍历
                for (int i = 0; i < fields.FieldCount; i++)
                {
                    //将当前要素的每个字段值放在数组的相应位置
                    strs[i] = feature.get_Value(i).ToString();
                }
                //在DataGridView中添加一行的数据
                dataGridView.Rows.Add(strs);
                //移动游标到下一个要素
                feature = featureCursor.NextFeature();
            }
        }


    }
}
