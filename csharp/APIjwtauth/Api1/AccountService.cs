using Api1.Models;
using Microsoft.AspNetCore.Identity;

namespace Api1
{
    public class AccountService(AccountRepository accountRepository, JWTService jwtService)
    {
        public void Register(string username, string email, string password, DateTime dateOfBirth)
        {
            var user = new User
            {
                Id = Guid.NewGuid(),
                Name = username,
                Email = email,
                DateOfBirth = dateOfBirth
            };
            var passwordHash = new PasswordHasher<User>().HashPassword(user, password);
            user.Password = passwordHash;
            accountRepository.Add(user);
        }

        public string Login(string username, string password)
        {
            var account = accountRepository.GetByEmail(username);
            var result = new PasswordHasher<User>().VerifyHashedPassword(account, account.Password, password);
            if (result == PasswordVerificationResult.Success)
            {
                return jwtService.GenerateToken(account);
            }
            else
            {
                throw new Exception("Unauthorized");
            }
        }
    }
}
