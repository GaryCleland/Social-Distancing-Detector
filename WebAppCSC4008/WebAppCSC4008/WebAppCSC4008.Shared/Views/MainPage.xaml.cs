using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.IO;
using System.Linq;
using System.Runtime.InteropServices.WindowsRuntime;
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

            Alerts.Add(Alert4);
            Alerts.Add(Alert5);
            Alerts.Add(Alert6);
            Alerts.Add(Alert7);
            Alerts.Add(Alert8);
            Alerts.Add(Alert9);
            Alerts.Add(Alert10);

            this.InitializeComponent();

            FilterModes.Add("Module");
            FilterModes.Add("Room");
            FilterModes.Add("University");
            FilterModes.Add("DateTime");
            FilterModes.Add("Lecturer");

            AlertView.ItemsSource = Alerts;
        }

        public Alert Alert4 = new Alert
        {
            ID = 4,
            University = "Queen's",
            Room = "CSB 02/27",
            Module = "CSC4006",
            Lecturer = "Dr. Barry McCollum",
            GroupSize = 4,
            DateTime = "18/11/2021 00:34:05",
            Duration = 11.585,
        };

        public Alert Alert5 = new Alert
        {
            ID = 5,
            University = "Queen's",
            Room = "CSB 02/27",
            Module = "CSC4006",
            Lecturer = "Dr. Barry McCollum",
            GroupSize = 3,
            DateTime = "18/11/2021 00:34:08",
            Duration = 2.49582,
        };

        public Alert Alert6 = new Alert
        {
            ID = 6,
            University = "Queen's",
            Room = "CSB 02/27",
            Module = "CSC4006",
            Lecturer = "Dr. Barry McCollum",
            GroupSize = 2,
            DateTime = "18/11/2021 00:34:11",
            Duration = 2.55424,
        };

        public Alert Alert7 = new Alert
        {
            ID = 7,
            University = "Queen's",
            Room = "CSB 02/27",
            Module = "CSC4006",
            Lecturer = "Dr. Barry McCollum",
            GroupSize = 5,
            DateTime = "18/11/2021 00:35:21",
            Duration = 2.24924,
        };

        public Alert Alert8 = new Alert
        {
            ID = 8,
            University = "Queen's",
            Room = "DKB 0G/118",
            Module = "CSC4008",
            Lecturer = "Dr. Jesus Martinez del Rincon",
            GroupSize = 2,
            DateTime = "18/11/2021 00:38:21",
            Duration = 2.46173,
        };

        public Alert Alert9 = new Alert
        {
            ID = 9,
            University = "Queen's",
            Room = "DKB 0G/118",
            Module = "CSC4008",
            Lecturer = "Dr. Jesus Martinez del Rincon",
            GroupSize = 3,
            DateTime = "18/11/2021 00:42:09",
            Duration = 3.51294,
        };

        public Alert Alert10 = new Alert
        {
            ID = 10,
            University = "Queen's",
            Room = "DKB 0G/118",
            Module = "CSC4008",
            Lecturer = "Dr. Jesus Martinez del Rincon",
            GroupSize = 4,
            DateTime = "18/11/2021 00:42:37",
            Duration = 5.9955,
        };

        public ObservableCollection<Alert> Alerts = new ObservableCollection<Alert>();

        public ObservableCollection<string> FilterModes = new ObservableCollection<string>();

        public List<Alert> FilteredAlerts = new List<Alert>();

        public string FilterMode;

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
                    FilteredAlerts = Alerts.Where(a => a.DateTime.ToString().ToLower().Contains(filterText)).ToList();
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
                    FilteredAlerts = Alerts.Where(a => a.DateTime.ToString().ToLower().Contains(filterText)).ToList();
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

    }
}
