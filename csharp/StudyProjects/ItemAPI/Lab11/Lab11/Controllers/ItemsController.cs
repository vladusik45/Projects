using Microsoft.AspNetCore.Mvc;

namespace Lab11.Controllers
{
    [ApiController]
    [Route("api/[controller]/[action]")]
    public class ItemsController : ControllerBase
    {
        private readonly List<Item> _items = new List<Item>
        {
        new Item { Id = 1, Name = "Item 1", Price = 10 },
        new Item { Id = 2, Name = "Item 2", Price = 20 },
        new Item { Id = 3, Name = "Item 3", Price = 30 }
        };

        [HttpGet]
        public IActionResult GetAllItems()
        {
            return Ok(_items);
        }

        [HttpGet("{id}")]
        public IActionResult GetItemById(int id)
        {
            var item = _items.FirstOrDefault(i => i.Id == id);
            if (item == null)
            {
                return NotFound();
            }
            return Ok(item);
        }

        [HttpPost]
        public IActionResult AddItem(Item item)
        {
            _items.Add(item);
            return CreatedAtAction(nameof(GetItemById), new { id = item.Id }, item);
        }

        [HttpPut("{id}")]
        public IActionResult UpdateItem(int id, Item item)
        {
            var existingItem = _items.FirstOrDefault(i => i.Id == id);
            if (existingItem == null)
            {
                return NotFound();
            }
            existingItem.Name = item.Name;
            existingItem.Price = item.Price;
            return NoContent();
        }

        [HttpDelete("{id}")]
        public IActionResult DeleteItem(int id)
        {
            var itemToRemove = _items.FirstOrDefault(i => i.Id == id);
            if (itemToRemove == null)
            {
                return NotFound();
            }
            _items.Remove(itemToRemove);
            return NoContent();
        }
    }
}
