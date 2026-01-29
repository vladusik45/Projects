using SupportTicketSystem.Models;

namespace SupportTicketSystem.Authorization
{
    public class UserRepository
    {
        private readonly ApplicationDbContext _context;

        public UserRepository(ApplicationDbContext context)
        {
            _context = context;
        }

        public void Add(User user)
        {
            _context.Users.Add(user);
            _context.SaveChanges();
        }

        public User? GetByUsername(string username)
        {
            User user = _context.Users.FirstOrDefault(u => u.Username == username);
            return user;
        }
    }
}
