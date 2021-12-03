using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.IO;
using System.Linq;
using System.Runtime.InteropServices.WindowsRuntime;
using System.Threading.Tasks;
using WebAppCSC4008.Data;
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
            FilteredAlerts = Alerts.ToList();
            AlertView.ItemsSource = FilteredAlerts;
        }

        public ObservableCollection<Alert> Alerts = new ObservableCollection<Alert>();

        public ObservableCollection<string> FilterModes = new ObservableCollection<string>();

        public List<Alert> FilteredAlerts = new List<Alert>();

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
            string filterText = (sender as TextBox).Text.ToLower();

            if (FilterMode != null)
            {
                if (FilterMode.Equals("Module"))
                {
                    FilteredAlerts = Alerts.Where(a => a.Module.ToLower().Contains(filterText)).ToList();
                }
                else if (FilterMode.Equals("Room"))
                {
                    FilteredAlerts = Alerts.Where(a => a.Room.ToLower().Contains(filterText)).ToList();
                }
                else if (FilterMode.Equals("University"))
                {
                    FilteredAlerts = Alerts.Where(a => a.University.ToLower().Contains(filterText)).ToList();
                }
                else if (FilterMode.Equals("DateTime"))
                {
                    FilteredAlerts = Alerts.Where(a => a.Date_time.ToLower().Contains(filterText)).ToList();
                }
                else if (FilterMode.Equals("Lecturer"))
                {
                    FilteredAlerts = Alerts.Where(a => a.Lecturer.ToLower().Contains(filterText)).ToList();
                }
                else if (FilterMode.Equals(""))
                {
                    FilteredAlerts = Alerts.ToList();
                }
            }

            AlertView.ItemsSource = FilteredAlerts;
        }

        private void FilterMode_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            FilterMode = (sender as ComboBox).SelectedItem as string;

            string filterText = FilterTextBox.Text.ToLower();

            if (FilterMode != null) {
                if (FilterMode.Equals("Module"))
                {
                    FilteredAlerts = Alerts.Where(a => a.Module.ToLower().Contains(filterText)).ToList();
                }
                else if (FilterMode.Equals("Room"))
                {
                    FilteredAlerts = Alerts.Where(a => a.Room.ToLower().Contains(filterText)).ToList();
                }
                else if (FilterMode.Equals("University"))
                {
                    FilteredAlerts = Alerts.Where(a => a.University.ToLower().Contains(filterText)).ToList();
                }
                else if (FilterMode.Equals("DateTime"))
                {
                    FilteredAlerts = Alerts.Where(a => a.Date_time.ToLower().Contains(filterText)).ToList();
                }
                else if (FilterMode.Equals("Lecturer"))
                {
                    FilteredAlerts = Alerts.Where(a => a.Lecturer.ToLower().Contains(filterText)).ToList();
                }
                else if (FilterMode.Equals(""))
                {
                    FilteredAlerts = Alerts.ToList();
                }
            }

            AlertView.ItemsSource = FilteredAlerts;
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            double size = FilteredAlerts[0].CFontSize;
            AlertView.ItemsSource = null;
            Alerts = new ObservableCollection<Alert>(App.AlertDatabase.GetDatabase().Table<Alert>().ToList());

            FilterMode = FilterModeBox.SelectedItem as string;

            string filterText = FilterTextBox.Text.ToLower();

                if (FilterMode == null)
                {
                    FilteredAlerts = Alerts.ToList();
                }
                else if (FilterMode.Equals("Module"))
                {
                    FilteredAlerts = Alerts.Where(a => a.Module.ToLower().Contains(filterText)).ToList();
                }
                else if (FilterMode.Equals("Room"))
                {
                    FilteredAlerts = Alerts.Where(a => a.Room.ToLower().Contains(filterText)).ToList();
                }
                else if (FilterMode.Equals("University"))
                {
                    FilteredAlerts = Alerts.Where(a => a.University.ToLower().Contains(filterText)).ToList();
                }
                else if (FilterMode.Equals("DateTime"))
                {
                    FilteredAlerts = Alerts.Where(a => a.Date_time.ToLower().Contains(filterText)).ToList();
                }
                else if (FilterMode.Equals("Lecturer"))
                {
                    FilteredAlerts = Alerts.Where(a => a.Lecturer.ToLower().Contains(filterText)).ToList();
                }
                else if (FilterMode.Equals(""))
                {
                    FilteredAlerts = Alerts.ToList();
                }

            foreach (Alert alert in FilteredAlerts)
            {
                alert.CFontSize = size;
            }
            AlertView.ItemsSource = FilteredAlerts;
        }

        private void Zoomin_Click(object sender, RoutedEventArgs e)
        {
            AlertView.ItemsSource = null;
            foreach (Alert alert in FilteredAlerts)
            {
                if (alert.CFontSize < 35)
                    alert.CFontSize += 2;
            }
            AlertView.ItemsSource = FilteredAlerts;
#if __WASM__ || NETFX_CORE
            if (FilteredAlerts[0].CFontSize >= 35)
                zoomin.IsEnabled = false;
            else
                zoomin.IsEnabled = true;
            if (FilteredAlerts[0].CFontSize > 2)
                zoomout.IsEnabled = true;
#endif
        }

        private void Zoomout_Click(object sender, RoutedEventArgs e)
        {
            AlertView.ItemsSource = null;
            foreach (Alert alert in FilteredAlerts)
            {
                if (alert.CFontSize > 2)
                    alert.CFontSize -= 2;
            }
            AlertView.ItemsSource = FilteredAlerts;
#if __WASM__ || NETFX_CORE
            if (FilteredAlerts[0].CFontSize <= 2)
                zoomout.IsEnabled = false;
            else
                zoomout.IsEnabled = true;
            if (FilteredAlerts[0].CFontSize < 35)
                zoomin.IsEnabled = true;
#endif
        }
    }
}
