using System;
using System.Net;
using System.Net.Sockets;
using System.Text;

class Program
{
    static void Main(string[] args)
    {
        IPAddress ipAddr = IPAddress.Loopback;
        IPEndPoint localEndPoint = new IPEndPoint(ipAddr, 8000);

        TcpListener listener = new TcpListener(localEndPoint);
        listener.Start();

        while (true)
        {
            Console.WriteLine("Waiting for a connection...");
            Socket clientSocket = null;
            try
            {
                clientSocket = listener.AcceptSocket();
                Console.WriteLine("Client connected.");
            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
            }

            byte[] bytes = new byte[1024];
            int numByte = clientSocket.Receive(bytes);

            string data = Encoding.ASCII.GetString(bytes, 0, numByte);
            Console.WriteLine("Message received -> {0}", data);

            byte[] message = Encoding.ASCII.GetBytes("Hello from server");
            clientSocket.Send(message);
        }
    }
}