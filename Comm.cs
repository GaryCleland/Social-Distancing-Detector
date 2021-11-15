using System;
using System.Net;
using System.Net.Sockets;
using System.Text;

public class SynchronousSocketListener {

    // Incoming data from the client.
    public static string data = null;

    public static void StartListening() {
        // Data buffer for incoming data.
        byte[] bytes = new Byte[1024];

        // Establish the local endpoint for socket.
        IPEndPoint localEndPoint = new IPEndPoint(IPAddress.Parse("127.0.0.1"), 51000);

        // Create a TCP/IP socket.
        Socket listener = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
        try {
            listener.Bind(localEndPoint);
            listener.Listen(10);

            // Start listening for connections.
            while (true) {
                Console.WriteLine("Waiting for a connection...");
                // Program is suspended while waiting for an incoming connection.
                Socket handler = listener.Accept();
                Console.WriteLine("Client Connected");
                data = null;

                // An incoming connection needs to be processed.
                int bytesRec = handler.Receive(bytes);
                data += Encoding.ASCII.GetString(bytes,0,bytesRec);

                // Show the data on the console.
                Console.WriteLine( "Text received : {0}", data);

                // TODO: Replace code below to shutdown when given a command
                handler.Shutdown(SocketShutdown.Both);
                handler.Close();
            }

        } catch (Exception e) {
            Console.WriteLine(e.ToString());
        }

        Console.WriteLine("\nPress ENTER to continue");
        Console.Read();

    }

    public static int Main(String[] args) {
        StartListening();
        return 0;
    }
}