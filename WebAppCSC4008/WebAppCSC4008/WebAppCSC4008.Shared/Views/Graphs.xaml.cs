using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Runtime.InteropServices.WindowsRuntime;
using Windows.Foundation;
using Windows.Foundation.Collections;
using Windows.UI.Xaml;
using Windows.UI.Xaml.Controls;
using Windows.UI.Xaml.Controls.Primitives;
using Windows.UI.Xaml.Data;
using Windows.UI.Xaml.Input;
using Windows.UI.Xaml.Media;
using Windows.UI.Xaml.Navigation;
using WebAppCSC4008.Models;
using Windows.UI.Xaml.Media.Imaging;

// The Blank Page item template is documented at https://go.microsoft.com/fwlink/?LinkId=234238

namespace WebAppCSC4008.Views
{
    /// <summary>
    /// An empty page that can be used on its own or navigated to within a Frame.
    /// </summary>
    public sealed partial class Graphs : Page
    {
        private List<string> graphs = new List<string>(GraphObject.graphs);
        private string graph = "";
        public Graphs()
        {
            this.InitializeComponent();

            App.NavigationFrame = this.ContentFrame;

            listView.ItemsSource = graphs;

            DataContext = this;
        }

        private void listView_ItemClick(object sender, ItemClickEventArgs e)
        {
            string image = "";
            graph = e.ClickedItem.ToString();
            if (graph == "Most Frequent Breach Location")
                image = "ms-appx:///Assets/testgraph.png";
            else if (graph == "Average Breach Duration Per Group")
                image = "ms-appx:///Assets/testgraph2.png";
            else
                image = "ms-appx:///Assets/testgraph3.png";
            imageSource = new BitmapImage(new Uri(image));
            graphimage.Source = imageSource;
        }

        public ImageSource imageSource { get; set; }
    }
}
