using Eghednevnik.Models;
using Eghednevnik.Services;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace Eghednevnik
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }
        private readonly string PATH = $"{Environment.CurrentDirectory}\\todoDatalist.json";
        private BindingList<ToDoModel> _todoData;
        private FileIO _fileIO;

        public void Window_Loaded(object sender, RoutedEventArgs e)
        {
            _fileIO = new FileIO(PATH);
            string proverka = new FileIO(PATH).ToString();
            if (proverka != "")
            {
                try
                {
                    _todoData = _fileIO.LoadData();
                }
                catch (Exception ex)
                {
                    MessageBox.Show(ex.Message);
                    Close();
                }
            }
            spisok.ItemsSource = _todoData;
            _todoData.ListChanged += _todoData_ListChanged;

            if (File.Exists("text.txt"))
            {
                Txt.Text = File.ReadAllText("text.txt");
            }
            if (File.Exists("date.txt"))
            {
                dte.Text = File.ReadAllText("date.txt");
            }
        }

        private void _todoData_ListChanged(object sender, ListChangedEventArgs e)
        {
                try
                {
                    _fileIO.SaveData(sender);
                }
                catch (Exception ex)
                {
                    MessageBox.Show(ex.Message);
                    Close();
                }
        }
        void SaveData(string txt, string pth)
        {
            if(txt.Count()>0)
            {
                if(File.Exists(pth)) 
                File.Create(pth).Close();
                File.WriteAllText(pth, txt);
            }
        }

        private void Window_Closed(object sender, EventArgs e)
        {
            SaveData(Txt.Text, "text.txt");
            SaveData(dte.Text, "date.txt");
        }
    }
}
