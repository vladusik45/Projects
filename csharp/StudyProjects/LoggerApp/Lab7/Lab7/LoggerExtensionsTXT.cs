namespace Lab7
{
    public static class LoggerExtensionsTXT
    {
        public static ILoggingBuilder AddFile(this ILoggingBuilder builder, string filePath)
        {
            builder.AddProvider(new LoggerProviderTXT(filePath));
            return builder;
        }
    }
}
