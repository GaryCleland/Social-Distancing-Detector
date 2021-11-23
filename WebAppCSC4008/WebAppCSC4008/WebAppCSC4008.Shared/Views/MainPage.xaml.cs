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
    }
}
