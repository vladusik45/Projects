using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Options;
using Microsoft.IdentityModel.Tokens;
using System.IdentityModel.Tokens.Jwt;
using System.Security.Claims;
using System.Text;

namespace test3.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class AccountController : Controller
    {
        private readonly JWTSettings _options;

        public AccountController(IOptions<JWTSettings> optAccess)
        {
            _options = optAccess.Value;
        }
        [HttpGet("GetToken")]
        public string GetToken()
        {
            List<Claim> claims = new List<Claim>();
            claims.Add(new Claim(ClaimTypes.Name, "Masha"));
            claims.Add(new Claim("Login", "12345"));
            claims.Add(new Claim(ClaimTypes.Role, "Admin"));

            var signingkey = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(_options.SecretKey));

            var jwt = new JwtSecurityToken(
                issuer: _options.Issuer,
                audience: _options.Audience,
                claims: claims,
                expires: DateTime.UtcNow.Add(TimeSpan.FromMinutes(1)),
                notBefore: DateTime.UtcNow,
                signingCredentials: new SigningCredentials(signingkey, SecurityAlgorithms.HmacSha256)
                    );
            return new JwtSecurityTokenHandler().WriteToken(jwt);
        }
    }
}
