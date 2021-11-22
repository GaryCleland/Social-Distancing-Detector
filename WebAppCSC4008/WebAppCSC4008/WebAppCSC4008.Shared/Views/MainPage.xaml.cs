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

            //var alerts = App.AlertDatabase.GetDatabase().Table<Alert>().ToList();

            Alerts = new ObservableCollection<Alert>(App.AlertDatabase.GetDatabase().Table<Alert>().ToList());

            AlertView.ItemsSource = Alerts;
        }

        public ObservableCollection<Alert> Alerts = new ObservableCollection<Alert>();

        public IEnumerable<Alert> GetAlerts()
        {
            return App.AlertDatabase.GetAlerts();
        }
    }
}
