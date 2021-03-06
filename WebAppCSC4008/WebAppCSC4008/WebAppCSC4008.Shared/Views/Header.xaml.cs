using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Runtime.InteropServices.WindowsRuntime;
using WebAppCSC4008.Views;
using Windows.Foundation;
using Windows.Foundation.Collections;
using Windows.UI.Xaml;
using Windows.UI.Xaml.Controls;
using Windows.UI.Xaml.Controls.Primitives;
using Windows.UI.Xaml.Data;
using Windows.UI.Xaml.Input;
using Windows.UI.Xaml.Media;
using Windows.UI.Xaml.Navigation;

// The User Control item template is documented at https://go.microsoft.com/fwlink/?LinkId=234236

namespace WebAppCSC4008
{
    public sealed partial class Header : UserControl
    {
        public Header()
        {
            this.InitializeComponent();
        }

        private void NavView_ItemInvoked(NavigationView sender, NavigationViewItemInvokedEventArgs args)
        {
            var item = args.InvokedItemContainer as NavigationViewItem;

			switch (item.Tag?.ToString() ?? string.Empty)
			{
				case "AlertsPage":
					App.NavigationFrame.Navigate(typeof(MainPage));
					break;

				case "CamerasPage":
					App.NavigationFrame.Navigate(typeof(CameraAvailability));
					break;

				case "GraphsPage":
					App.NavigationFrame.Navigate(typeof(Graphs));
					break;
			}
		}

		public bool ShowNavBar
		{
			get { return (bool)GetValue(ShowNavBarProperty); }
			set { SetValue(ShowNavBarProperty, value); }
		}

		public static readonly DependencyProperty ShowNavBarProperty =
			DependencyProperty.Register("ShowNavBar", typeof(bool), typeof(Header), new PropertyMetadata(true));

		public string PageTitle
		{
			get { return (string)GetValue(PageTitleProperty); }
			set { SetValue(PageTitleProperty, value); }
		}

		public static readonly DependencyProperty PageTitleProperty =
			DependencyProperty.Register("PageTitle", typeof(string), typeof(Header), new PropertyMetadata(null));
	}
}
