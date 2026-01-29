using Api1.Models;
using Microsoft.Extensions.Options;
using Microsoft.IdentityModel.Tokens;
using System.Data;
using System.IdentityModel.Tokens.Jwt;
using System.Security.Claims;
using System.Text;

namespace Api1
{
    public class JWTService(IOptions<AuthSettings> options)
    {
        public string GenerateToken(User user)
        {
            var role = "Admin";
            var claims = new List<Claim>
            {
                new Claim("username", user.Name),
                new Claim("email", user.Email),
                new Claim("date", user.DateOfBirth.ToString()),
                new Claim(ClaimTypes.Role, role)
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
