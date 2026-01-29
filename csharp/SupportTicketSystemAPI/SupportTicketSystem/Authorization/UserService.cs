using Microsoft.AspNetCore.Identity;
using SupportTicketSystem.Models;

namespace SupportTicketSystem.Authorization
{
    public class UserService(UserRepository userRepository, JWTService jwtService)
    {
        public void Register(string username, string password, string role)
        {
            var user = new User
            {
                Id = Guid.NewGuid(),
                Username = username,
                Role = role
            };
            var passwordHash = new PasswordHasher<User>().HashPassword(user, password);
            user.PasswordHash = passwordHash;
            userRepository.Add(user);
        }

        public string Login(string username, string password)
        {
            var user = userRepository.GetByUsername(username);
            if (user != null) 
            { 
                var result = new PasswordHasher<User>().VerifyHashedPassword(user, user.PasswordHash, password);
                if (result == PasswordVerificationResult.Success)
                {
                    return jwtService.GenerateToken(user);
                }
            }
            return null;
            
        }
    }
}
