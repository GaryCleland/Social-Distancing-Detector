using Tizen.Applications;
using Uno.UI.Runtime.Skia;

namespace WebAppCSC4008.Skia.Tizen
{
    class Program
    {
        static void Main(string[] args)
        {
            var host = new TizenHost(() => new WebAppCSC4008.App(), args);
            host.Run();
        }
    }
}
