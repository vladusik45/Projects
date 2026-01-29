using SupportTicketSystem.Models;

namespace SupportTicketSystem
{
    public class AdminService
    {
        private readonly ApplicationDbContext _context;

        public AdminService(ApplicationDbContext context)
        {
            _context = context;
        }
        public User ChangeRole(string username, string role)
        {
            var user = _context.Users.FirstOrDefault(u => u.Username == username);
            if (user != null)
            {
                user.Role = role;
                _context.SaveChanges();
            }
            return user;
        }
    }
}
