using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.IO;
using System.Linq;
using System.Runtime.InteropServices.WindowsRuntime;
using System.Threading.Tasks;
using WebAppCSC4008.Models;
using Windows.Foundation;
using Windows.Foundation.Collections;
using Windows.UI.Xaml;
using Windows.UI.Xaml.Controls;
using Windows.UI.Xaml.Controls.Primitives;
using Windows.UI.Xaml.Data;
using Windows.UI.Xaml.Input;
using Windows.UI.Xaml.Media;
using Windows.UI.Xaml.Navigation;

// The Blank Page item template is documented at http://go.microsoft.com/fwlink/?LinkId=402352&clcid=0x409

namespace WebAppCSC4008
{
    /// <summary>
    /// An empty page that can be used on its own or navigated to within a Frame.
    /// </summary>
    public sealed partial class MainPage : Page
    {
        public MainPage()
        {
            this.InitializeComponent();

            FilterModes.Add("Module");
            FilterModes.Add("Room");
            FilterModes.Add("University");
            FilterModes.Add("DateTime");
            FilterModes.Add("Lecturer");

            FilterMode = "";

#if __WASM__
            Alerts.Add(Alert1);
            Alerts.Add(Alert2);
            Alerts.Add(Alert3);
#else
            Alerts = new ObservableCollection<Alert>(App.AlertDatabase.GetDatabase().Table<Alert>().ToList());
#endif

            AlertView.ItemsSource = Alerts;
        }

        public ObservableCollection<Alert> Alerts = new ObservableCollection<Alert>();

        public ObservableCollection<string> FilterModes = new ObservableCollection<string>();

        public string FilterMode;

        public Alert Alert1 = new Alert
        {
            DisplayID = 523,
            University = "Queen's University Belfast",
            Room = "CSB 02/027",
            Module = "CSC4008",
            Lecturer = "Dr. Barry McCollum",
            Group_size = 2,
            Date_time = "10/11/2021 10:43:12",
            Duration = 2057,
        };

        public Alert Alert2 = new Alert
        {
            DisplayID = 527,
            University = "Queen's University Belfast",
            Room = "ASH 09/005",
            Module = "CSC4005",
            Lecturer = "Dr. Blesson Varghese",
            Group_size = 12,
            Date_time = "10/11/2021 16:01:02",
            Duration = 305,
        };

        public Alert Alert3 = new Alert
        {
            DisplayID = 463,
            University = "Queen's University Belfast",
            Room = "DKB 0G/115",
            Module = "CSC4008",
            Lecturer = "Dr. Barry McCollum",
            Group_size = 3,
            Date_time = "09/10/2021 12:00:23",
            Duration = 969,
        };

        private void TextFilter_TextChanged(object sender, TextChangedEventArgs e)
        {
            string filterText = (sender as TextBox).Text;
            List<Alert> filteredAlerts = new List<Alert>();

            if (FilterMode.Equals("Module"))
            {
                filteredAlerts = Alerts.Where(a => a.Module.Contains(filterText)).ToList();
            }
            else if (FilterMode.Equals("Room"))
            {
                filteredAlerts = Alerts.Where(a => a.Room.Contains(filterText)).ToList();
            }
            else if (FilterMode.Equals("University"))
            {
                filteredAlerts = Alerts.Where(a => a.University.Contains(filterText)).ToList();
            }
            else if (FilterMode.Equals("DateTime"))
            {
                filteredAlerts = Alerts.Where(a => a.Date_time.Contains(filterText)).ToList();
            }
            else if (FilterMode.Equals("Lecturer"))
            {
                filteredAlerts = Alerts.Where(a => a.Lecturer.Contains(filterText)).ToList();
            }
            else if (FilterMode.Equals(""))
            {
                filteredAlerts = Alerts.ToList();
            }

            AlertView.ItemsSource = filteredAlerts;
        }

        private void FilterMode_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            FilterMode = (sender as ComboBox).SelectedItem as string;

            string filterText = FilterTextBox.Text;
            List<Alert> filteredAlerts = new List<Alert>();

            if (FilterMode.Equals("Module"))
            {
                filteredAlerts = Alerts.Where(a => a.Module.Contains(filterText)).ToList();
            }
            else if (FilterMode.Equals("Room"))
            {
                filteredAlerts = Alerts.Where(a => a.Room.Contains(filterText)).ToList();
            }
            else if (FilterMode.Equals("University"))
            {
                filteredAlerts = Alerts.Where(a => a.University.Contains(filterText)).ToList();
            }
            else if (FilterMode.Equals("DateTime"))
            {
                filteredAlerts = Alerts.Where(a => a.Date_time.Contains(filterText)).ToList();
            }
            else if (FilterMode.Equals("Lecturer"))
            {
                filteredAlerts = Alerts.Where(a => a.Lecturer.Contains(filterText)).ToList();
            }
            else if (FilterMode.Equals(""))
            {
                filteredAlerts = Alerts.ToList();
            }

            AlertView.ItemsSource = filteredAlerts;
        }
    }
}
