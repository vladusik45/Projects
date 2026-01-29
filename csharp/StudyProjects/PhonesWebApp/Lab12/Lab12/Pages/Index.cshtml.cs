using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.EntityFrameworkCore;
using System.Collections;

namespace Lab12.Pages
{
    public class IndexModel : PageModel
    {
        private readonly ILogger<IndexModel> _logger;

        public IList<Phone> _phones { get; set; }

        public IndexModel(ILogger<IndexModel> logger)
        {
            _logger = logger;
        }


        public void OnGet()
        {
            using (ApplicationContext db = new ApplicationContext())
            {
                db.phones.Add(new Phone
                {
                    brand = "Google",
                    model = "Pixel 8 Pro",
                    price = 1005
                });
                db.phones.Add(new Phone
                {
                    brand = "Apple",
                    model = "Iphone X",
                    price = 1206
                });
                db.phones.Add(new Phone
                {
                    brand = "Samsung",
                    model = "Galaxy S24 Ultra",
                    price = 90
                });
                db.SaveChanges();
                _phones = db.phones.ToList();
            }
        }
    }
}