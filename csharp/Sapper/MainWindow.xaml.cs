using System.Windows;
using System.Windows.Controls;
using System.Windows.Input;

namespace Sweeper
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            DataContext = new MinesweeperViewModel();
        }
        private void MouseRightButtonUpHandler(object sender, MouseButtonEventArgs e)
        {
            var viewModel = DataContext as MinesweeperViewModel;
            if (viewModel != null) 
            {
                var button = e.Source as Button;
                if (button != null) 
                {
                    var cell = button.Tag as Cell;
                    viewModel.CellRightClickCommand.Execute(cell);
                }
            }
        }
    }
}
