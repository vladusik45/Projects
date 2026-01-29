using System.Diagnostics.Eventing.Reader;
using System.Text.Json;

namespace Lab7
{
    public class LoggerTXT : ILogger, IDisposable
    {
        string filePath1;
        string filePath2;
        static object _lock = new object();
        public LoggerTXT(string path)
        {
            if (path.Contains(".json"))
                filePath1 = path;
            else
                filePath2 = path;
        }
        public IDisposable BeginScope<TState>(TState state)
        {
            return this;
        }

        public void Dispose() { }

        public bool IsEnabled(LogLevel logLevel)
        {
            return true;
        }

        public void Log<TState>(LogLevel logLevel, EventId eventId,
                    TState state, Exception? exception, Func<TState, Exception?, string> formatter)
        {
            var jsonLine = JsonSerializer.Serialize(new
            {
                logLevel,
                eventId,
                parameters = (state as IEnumerable<KeyValuePair<string, object>>)?.ToDictionary(i => i.Key, i => i.Value),
                message = formatter(state, exception),
                exception = exception?.GetType().Name
            });

            lock (_lock)
            {
                if (filePath1 != null)
                    File.AppendAllText(filePath1, jsonLine + Environment.NewLine);
                if(filePath2 != null)
                    File.AppendAllText(filePath2, formatter(state, exception) + Environment.NewLine);
            }
        }

    }
}
