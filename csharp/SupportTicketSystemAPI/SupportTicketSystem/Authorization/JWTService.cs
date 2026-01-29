using Microsoft.Extensions.Options;
using Microsoft.IdentityModel.Tokens;
using SupportTicketSystem.Models;
using System.IdentityModel.Tokens.Jwt;
using System.Security.Claims;
using System.Text;

namespace SupportTicketSystem.Authorization
{
    public class JWTService(IOptions<AuthSettings> options)
    {
        public string GenerateToken(User user)
        {
            var claims = new List<Claim>
            {
                new Claim("username", user.Username),
                new Claim(ClaimTypes.Role, user.Role)
            };
            var jwttoken = new JwtSecurityToken(
                expires: DateTime.UtcNow.Add(options.Value.Expires),
                claims: claims,
                signingCredentials: new SigningCredentials(
                    new SymmetricSecurityKey(Encoding.UTF8.GetBytes(options.Value.SecretKey)),
                    SecurityAlgorithms.HmacSha256));
            return new JwtSecurityTokenHandler().WriteToken(jwttoken);
        }
    }
}
