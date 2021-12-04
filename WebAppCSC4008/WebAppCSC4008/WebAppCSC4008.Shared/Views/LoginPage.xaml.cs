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
    public sealed partial class LoginPage : Page
    {
        public LoginPage()
        {
            this.InitializeComponent();

            App.NavigationFrame = this.ContentFrame;
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            string testUsername = "user";
            string testPassword = "password";
            string username = userTextBox.Text;
            string password = passTextBox.Password;
            if (username == testUsername && password == testPassword)
            {
                loginTextBlock.Text = String.Format("Login Sucessful\nWelcome : {0}", username);
                App.NavigationFrame.Navigate(typeof(MainPage));
            }
            else
            {
                loginTextBlock.Text = "Incorrect username or password, please try again.";
            }
        }
    }
}
