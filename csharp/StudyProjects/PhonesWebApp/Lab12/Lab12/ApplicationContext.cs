using Microsoft.EntityFrameworkCore;

namespace Lab12
{
    public class ApplicationContext : DbContext
    {
        public DbSet<Phone> phones => Set<Phone>();

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            optionsBuilder.UseNpgsql("Host=localhost;Port=5432;Database=postgres;Username=postgres;Password=5432;");
            optionsBuilder.LogTo(Console.WriteLine, LogLevel.Information);
        }
    }
}
