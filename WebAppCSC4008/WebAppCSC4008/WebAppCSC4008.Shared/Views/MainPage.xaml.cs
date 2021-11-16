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
            Alert Alert1 = new Alert
            {
                ID = 523,
                University = "Queen's University Belfast",
                Room = "CSB 02/027",
                Module = "CSC4008",
                Lecturer = "Dr. Barry McCollum",
                GroupSize = 2,
                DateTime = new DateTime(2021, 11, 10, 10, 43, 12),
                Duration = new TimeSpan(0, 34, 17),
            };
            Alerts.Add(Alert1);
            Alerts.Add(Alert2);
            Alerts.Add(Alert3);

            this.InitializeComponent();

            AlertView.ItemsSource = Alerts;
        }

        public Alert Alert1 = new Alert
        {
            ID = 523,
            University = "Queen's University Belfast",
            Room = "CSB 02/027",
            Module = "CSC4008",
            Lecturer = "Dr. Barry McCollum",
            GroupSize = 2,
            DateTime = new DateTime(2021, 11, 10, 10, 43, 12),
            Duration = new TimeSpan(0, 34, 17),
        };

        public Alert Alert2 = new Alert
        {
            ID = 527,
            University = "Queen's University Belfast",
            Room = "ASH 09/005",
            Module = "CSC4005",
            Lecturer = "Dr. Blesson Varghese",
            GroupSize = 12,
            DateTime = new DateTime(2021, 11, 10, 16, 01, 2),
            Duration = new TimeSpan(0, 5, 5),
        };

        public Alert Alert3 = new Alert
        {
            ID = 463,
            University = "Queen's University Belfast",
            Room = "DKB 0G/115",
            Module = "CSC4008",
            Lecturer = "Dr. Barry McCollum",
            GroupSize = 3,
            DateTime = new DateTime(2021, 10, 9, 12, 00, 23),
            Duration = new TimeSpan(0, 16, 9),
        };

        public ObservableCollection<Alert> Alerts = new ObservableCollection<Alert>();

    }
}
