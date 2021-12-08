using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Runtime.InteropServices.WindowsRuntime;
using WebAppCSC4008.Models;
using WebAppCSC4008.Output;
using Windows.Foundation;
using Windows.Foundation.Collections;
using Windows.UI.Xaml;
using Windows.UI.Xaml.Controls;
using Windows.UI.Xaml.Controls.Primitives;
using Windows.UI.Xaml.Data;
using Windows.UI.Xaml.Input;
using Windows.UI.Xaml.Media;
using Windows.UI.Xaml.Navigation;

// The Blank Page item template is documented at https://go.microsoft.com/fwlink/?LinkId=234238

namespace WebAppCSC4008
{
    /// <summary>
    /// An empty page that can be used on its own or navigated to within a Frame.
    /// </summary>
    public sealed partial class CameraAvailability : Page
    {
        private List<Camera> cams = new List<Camera>(Camera.cameras());
        private Random rand = new Random();
        public CameraAvailability()
        {
            this.InitializeComponent();

            App.NavigationFrame = this.ContentFrame;

            dataGrid.ItemsSource = cams;
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            string text = TextBox1.Text;
            cams.Add(new Camera(cams.Count+1, text, status(rand.Next(0,1)), "DKB 0G/118", "Queen's University Belfast"));
            dataGrid.ItemsSource = null;
            dataGrid.ItemsSource = cams;
            if (!string.IsNullOrEmpty(text))
            {
                CameraDatabase cameraDatabase = new CameraDatabase(text);
            }
            TextBox1.Text = "";
        }

        private string room(int id)
        {
            List<string> list = new List<string>();
            list.Add("CSB 01/16");
            list.Add("ASH 07/27");
            list.Add("DKB 01/11");
            return list[id];
        }

        private string status(int id)
        {
            List<string> list = new List<string>();
            list.Add("Online");
            list.Add("Offline");
            return list[id];
        }
    }
}
