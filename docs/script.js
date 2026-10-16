const products = [
  { name: 'Innovative Ladder', price: 1500, icon: 'IL' },
  { name: 'Multipurpose Axe', price: 1500, icon: 'AX' },
  { name: 'Smokeless Bukhari', price: 10000, icon: 'SB' },
  { name: 'Walnut Cracker', price: 50000, icon: 'WC' }
];

const money = value => `₹${Number(value).toLocaleString('en-IN')}`;
const productGrid = document.querySelector('#productGrid');
const productSelect = document.querySelector('#product');
const quantity = document.querySelector('#quantity');
const total = document.querySelector('#total');
const form = document.querySelector('#orderForm');
const message = document.querySelector('#message');

products.forEach((item, index) => {
  productGrid.insertAdjacentHTML('beforeend', `
    <article class="product">
      <div class="icon">${item.icon}</div>
      <div><h3>${item.name}</h3><span class="price">${money(item.price)}</span></div>
    </article>
  `);
  productSelect.insertAdjacentHTML('beforeend', `<option value="${index}">${item.name} — ${money(item.price)}</option>`);
});

function updateTotal() {
  const item = products[Number(productSelect.value)];
  const qty = Math.max(1, Number(quantity.value) || 1);
  total.textContent = money(item.price * qty);
}

productSelect.addEventListener('change', updateTotal);
quantity.addEventListener('input', updateTotal);

form.addEventListener('submit', event => {
  event.preventDefault();
  const customer = document.querySelector('#customer').value.trim();
  const item = products[Number(productSelect.value)];
  const qty = Math.max(1, Number(quantity.value) || 1);
  const orderId = `RI-${Date.now().toString().slice(-8)}`;
  const order = { orderId, customer, product: item.name, quantity: qty, total: item.price * qty, createdAt: new Date().toISOString() };

  const orders = JSON.parse(localStorage.getItem('ri_demo_orders') || '[]');
  orders.unshift(order);
  localStorage.setItem('ri_demo_orders', JSON.stringify(orders.slice(0, 10)));

  message.textContent = `✓ Sample order ${orderId} created for ${customer}.`;
  message.style.color = '#087443';
  form.reset();
  quantity.value = 1;
  updateTotal();
});

updateTotal();
