namespace Lab7
{
    public class LoggerProviderTXT : ILoggerProvider
    {
        string path;
        public LoggerProviderTXT(string path)
        {
            this.path = path;
        }
        public ILogger CreateLogger(string categoryName)
        {
            return new LoggerTXT(path);
        }

        public void Dispose() { }
    }
}
