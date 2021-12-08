using System;
using System.Collections.Generic;
using System.Text;
using Windows.UI.Xaml.Data;

namespace WebAppCSC4008.Converters
{
    public class TwoDecimalPointConverter : IValueConverter
    {
        public object Convert(object value, Type targetType, object parameter, string language)
        {
            double duration;
            Double.TryParse(value.ToString(), out duration);
            duration = Math.Round(duration, 2);
            return duration;
        }

        public object ConvertBack(object value, Type targetType, object parameter, string language)
        {
            throw new NotImplementedException();
        }
    }
}