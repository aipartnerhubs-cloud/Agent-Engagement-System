"""
============================================================
🎨 POSTERS PORTAL HTML TEMPLATE
============================================================
Beautiful web portal for agents to browse and download posters
Mobile-responsive, professional design
============================================================
"""

POSTERS_PORTAL_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>🎨 Posters Portal | PB Partners</title>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:wght@700;900&family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  :root {
    --pb-blue: #0056d2;
    --pb-blue-dark: #002966;
    --pb-gold: #ffd700;
    --pb-green: #25d366;
    --pb-red: #ef4444;
    --pb-orange: #f97316;
    --pb-purple: #8b5cf6;
    --cream: #fdfbf5;
    --ink: #0a1628;
    --ink-soft: #4a5568;
  }
  body { 
    background: var(--cream); 
    color: var(--ink); 
    font-family: 'Inter', sans-serif; 
    line-height: 1.6;
    min-height: 100vh;
  }
  
  .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
  
  /* HEADER */
  .header {
    background: linear-gradient(135deg, var(--pb-purple), var(--pb-blue));
    color: white;
    border-radius: 24px;
    padding: 40px 30px;
    margin-bottom: 24px;
    position: relative;
    overflow: hidden;
    box-shadow: 0 20px 50px rgba(139, 92, 246, 0.3);
  }
  
  .header::before {
    content: '🎨';
    position: absolute;
    top: 10px;
    right: 25px;
    font-size: 120px;
    opacity: 0.12;
    line-height: 1;
  }
  
  .badge {
    display: inline-block;
    background: var(--pb-gold);
    color: var(--pb-blue-dark);
    padding: 6px 18px;
    border-radius: 30px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    letter-spacing: 3px;
    font-weight: 700;
    margin-bottom: 14px;
  }
  
  .header h1 {
    font-family: 'Fraunces', serif;
    font-size: 38px;
    font-weight: 900;
    line-height: 1.0;
    margin-bottom: 8px;
    letter-spacing: -1.5px;
  }
  
  .header h1 .gold { color: var(--pb-gold); font-style: italic; }
  
  .header p {
    font-size: 15px;
    opacity: 0.95;
    max-width: 600px;
  }
  
  .stats-row {
    display: flex;
    gap: 12px;
    margin-top: 16px;
    flex-wrap: wrap;
  }
  
  .stat-badge {
    background: rgba(255,255,255,0.2);
    backdrop-filter: blur(10px);
    padding: 8px 16px;
    border-radius: 14px;
    font-size: 13px;
    font-weight: 600;
    border: 1px solid rgba(255,215,0,0.3);
  }
  
  /* HOW TO USE */
  .howto {
    background: white;
    border-radius: 20px;
    padding: 24px;
    margin-bottom: 24px;
    box-shadow: 0 6px 20px rgba(10, 22, 40, 0.06);
  }
  
  .howto h2 {
    font-family: 'Fraunces', serif;
    font-size: 22px;
    margin-bottom: 12px;
    color: var(--pb-blue-dark);
  }
  
  .steps {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 12px;
    margin-top: 12px;
  }
  
  .step {
    background: var(--cream);
    padding: 14px 16px;
    border-radius: 12px;
    border-left: 4px solid var(--pb-blue);
  }
  
  .step-num {
    background: var(--pb-blue);
    color: white;
    width: 28px;
    height: 28px;
    border-radius: 50%;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-weight: 800;
    font-size: 13px;
    margin-right: 8px;
  }
  
  .step strong {
    color: var(--pb-blue-dark);
    font-size: 13px;
  }
  
  .step p {
    font-size: 12px;
    color: var(--ink-soft);
    margin-top: 4px;
  }
  
  /* FILTER */
  .filter-bar {
    display: flex;
    gap: 8px;
    margin-bottom: 20px;
    overflow-x: auto;
    padding: 4px;
  }
  
  .filter-btn {
    background: white;
    border: 2px solid #e2e8f0;
    color: var(--ink-soft);
    padding: 10px 16px;
    border-radius: 12px;
    font-size: 13px;
    font-weight: 600;
    cursor: pointer;
    white-space: nowrap;
    transition: all 0.2s;
    font-family: 'Inter', sans-serif;
  }
  
  .filter-btn:hover { border-color: var(--pb-blue); }
  
  .filter-btn.active {
    background: var(--pb-blue);
    color: white;
    border-color: var(--pb-blue);
    box-shadow: 0 4px 12px rgba(0, 86, 210, 0.3);
  }
  
  /* POSTERS GRID */
  .posters-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 16px;
  }
  
  .poster-card {
    background: white;
    border-radius: 18px;
    overflow: hidden;
    box-shadow: 0 6px 20px rgba(10, 22, 40, 0.08);
    transition: transform 0.2s, box-shadow 0.2s;
    border: 2px solid transparent;
  }
  
  .poster-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 30px rgba(10, 22, 40, 0.15);
    border-color: var(--pb-gold);
  }
  
  .poster-preview {
    height: 200px;
    background: linear-gradient(135deg, var(--pb-purple), var(--pb-blue));
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    overflow: hidden;
  }
  
  .poster-preview.blue { background: linear-gradient(135deg, #1e40af, #3b82f6); }
  .poster-preview.red { background: linear-gradient(135deg, #b91c1c, #ef4444); }
  .poster-preview.green { background: linear-gradient(135deg, #047857, #10b981); }
  .poster-preview.orange { background: linear-gradient(135deg, #c2410c, #f97316); }
  .poster-preview.gold { background: linear-gradient(135deg, #b45309, #f59e0b); }
  .poster-preview.pink { background: linear-gradient(135deg, #be185d, #ec4899); }
  .poster-preview.warm { background: linear-gradient(135deg, #92400e, #d97706); }
  .poster-preview.black { background: linear-gradient(135deg, #1e293b, #475569); }
  .poster-preview.white { background: linear-gradient(135deg, #f8fafc, #e2e8f0); color: var(--ink); }
  .poster-preview.tricolor { background: linear-gradient(180deg, #ff9933 33%, white 33% 66%, #138808 66%); }
  
  .poster-icon {
    font-size: 90px;
    filter: drop-shadow(0 8px 20px rgba(0,0,0,0.3));
  }
  
  .poster-card-id {
    position: absolute;
    top: 12px;
    right: 12px;
    background: rgba(0,0,0,0.4);
    backdrop-filter: blur(10px);
    color: white;
    padding: 4px 10px;
    border-radius: 12px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    font-weight: 700;
  }
  
  .poster-card-content {
    padding: 18px;
  }
  
  .poster-category {
    display: inline-block;
    background: var(--cream);
    color: var(--pb-blue);
    padding: 3px 10px;
    border-radius: 8px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.5px;
    margin-bottom: 8px;
  }
  
  .poster-title {
    font-family: 'Fraunces', serif;
    font-size: 18px;
    font-weight: 800;
    color: var(--pb-blue-dark);
    margin-bottom: 4px;
    line-height: 1.2;
  }
  
  .poster-style {
    font-size: 12px;
    color: var(--ink-soft);
    margin-bottom: 12px;
  }
  
  .poster-tool {
    display: inline-block;
    background: linear-gradient(135deg, var(--pb-gold), #f59e0b);
    color: var(--pb-blue-dark);
    padding: 3px 10px;
    border-radius: 8px;
    font-size: 10px;
    font-weight: 700;
    margin-bottom: 12px;
  }
  
  .poster-actions {
    display: flex;
    gap: 8px;
  }
  
  .btn {
    flex: 1;
    padding: 10px 14px;
    border-radius: 10px;
    font-size: 13px;
    font-weight: 700;
    border: none;
    cursor: pointer;
    text-align: center;
    transition: all 0.2s;
    font-family: 'Inter', sans-serif;
  }
  
  .btn-primary {
    background: var(--pb-blue);
    color: white;
  }
  
  .btn-primary:hover {
    background: var(--pb-blue-dark);
  }
  
  .btn-secondary {
    background: var(--pb-green);
    color: white;
  }
  
  .btn-secondary:hover {
    background: #1ea954;
  }
  
  /* MODAL */
  .modal {
    display: none;
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(0,0,0,0.7);
    backdrop-filter: blur(10px);
    z-index: 1000;
    align-items: center;
    justify-content: center;
    padding: 20px;
  }
  
  .modal.active {
    display: flex;
  }
  
  .modal-content {
    background: white;
    border-radius: 24px;
    padding: 28px;
    max-width: 700px;
    width: 100%;
    max-height: 90vh;
    overflow-y: auto;
    position: relative;
  }
  
  .modal-close {
    position: absolute;
    top: 16px;
    right: 16px;
    background: var(--cream);
    border: none;
    width: 36px;
    height: 36px;
    border-radius: 50%;
    font-size: 18px;
    font-weight: 700;
    cursor: pointer;
    color: var(--ink);
  }
  
  .modal-title {
    font-family: 'Fraunces', serif;
    font-size: 24px;
    font-weight: 800;
    color: var(--pb-blue-dark);
    margin-bottom: 6px;
    padding-right: 50px;
  }
  
  .modal-category {
    font-size: 13px;
    color: var(--ink-soft);
    margin-bottom: 18px;
  }
  
  .prompt-box {
    background: #1e293b;
    color: #e2e8f0;
    padding: 18px;
    border-radius: 14px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    line-height: 1.7;
    margin: 14px 0;
    max-height: 250px;
    overflow-y: auto;
    border-left: 4px solid var(--pb-gold);
  }
  
  .modal-tool {
    background: linear-gradient(135deg, var(--pb-gold), #f59e0b);
    color: var(--pb-blue-dark);
    padding: 8px 16px;
    border-radius: 12px;
    font-size: 12px;
    font-weight: 700;
    display: inline-block;
    margin-bottom: 12px;
  }
  
  .modal-instructions {
    background: var(--cream);
    padding: 16px;
    border-radius: 12px;
    margin: 16px 0;
    font-size: 13px;
  }
  
  .modal-instructions h4 {
    font-family: 'Fraunces', serif;
    color: var(--pb-blue-dark);
    margin-bottom: 8px;
  }
  
  .modal-instructions ol {
    margin-left: 18px;
  }
  
  .modal-instructions li {
    margin-bottom: 4px;
  }
  
  .modal-actions {
    display: flex;
    gap: 10px;
    margin-top: 18px;
  }
  
  .modal-actions .btn {
    padding: 12px;
  }
  
  /* TOAST */
  .toast {
    position: fixed;
    bottom: 30px;
    left: 50%;
    transform: translateX(-50%);
    background: var(--pb-green);
    color: white;
    padding: 14px 24px;
    border-radius: 12px;
    font-weight: 600;
    box-shadow: 0 10px 30px rgba(37, 211, 102, 0.4);
    z-index: 2000;
    opacity: 0;
    transition: opacity 0.3s, transform 0.3s;
  }
  
  .toast.show {
    opacity: 1;
    transform: translateX(-50%) translateY(-10px);
  }
  
  /* FOOTER */
  .footer {
    background: linear-gradient(135deg, var(--pb-blue-dark), var(--pb-blue));
    color: white;
    border-radius: 20px;
    padding: 26px;
    margin-top: 30px;
    text-align: center;
  }
  
  .footer h3 {
    font-family: 'Fraunces', serif;
    font-size: 22px;
    margin-bottom: 6px;
  }
  
  .footer p {
    opacity: 0.9;
    font-size: 14px;
  }
  
  .footer .contact {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: var(--pb-green);
    color: white;
    padding: 10px 20px;
    border-radius: 12px;
    margin-top: 14px;
    font-weight: 700;
    text-decoration: none;
  }
  
  @media (max-width: 600px) {
    .header h1 { font-size: 28px; }
    .header { padding: 28px 22px; }
    .posters-grid { grid-template-columns: 1fr 1fr; gap: 10px; }
    .poster-preview { height: 140px; }
    .poster-icon { font-size: 60px; }
    .poster-card-content { padding: 12px; }
    .poster-title { font-size: 14px; }
  }
  
  @media (max-width: 400px) {
    .posters-grid { grid-template-columns: 1fr; }
  }
</style>
</head>
<body>

<div class="container">

  <!-- HEADER -->
  <div class="header">
    <div class="badge">// MARKETING ARSENAL · 30 POSTERS</div>
    <h1>Posters <span class="gold">Portal</span></h1>
    <p>30 ready-made AI prompts. Copy → Paste → Generate. Apna naam edit karke customers ko bhejo!</p>
    
    <div class="stats-row">
      <div class="stat-badge">✓ {{ total }} Posters</div>
      <div class="stat-badge">✓ 6 Categories</div>
      <div class="stat-badge">✓ FREE Tools</div>
      <div class="stat-badge">✓ Editable</div>
    </div>
  </div>

  <!-- HOW TO USE -->
  <div class="howto">
    <h2>🚀 How to Use (4 Easy Steps)</h2>
    <div class="steps">
      <div class="step">
        <span class="step-num">1</span>
        <strong>Choose Poster</strong>
        <p>Browse 30 posters below</p>
      </div>
      <div class="step">
        <span class="step-num">2</span>
        <strong>Copy Prompt</strong>
        <p>Click "View" → Copy text</p>
      </div>
      <div class="step">
        <span class="step-num">3</span>
        <strong>Generate Image</strong>
        <p>Paste in Ideogram or Designer (FREE)</p>
      </div>
      <div class="step">
        <span class="step-num">4</span>
        <strong>Share</strong>
        <p>Edit name + WhatsApp to customers!</p>
      </div>
    </div>
  </div>

  <!-- FILTER -->
  <div class="filter-bar">
    <button class="filter-btn active" onclick="filterPosters('all')">🎨 All Posters</button>
    <button class="filter-btn" onclick="filterPosters('car')">🚗 Car</button>
    <button class="filter-btn" onclick="filterPosters('bike')">🏍️ Bike</button>
    <button class="filter-btn" onclick="filterPosters('health')">❤️ Health</button>
    <button class="filter-btn" onclick="filterPosters('family')">👨‍👩‍👧 Family</button>
    <button class="filter-btn" onclick="filterPosters('travel')">✈️ Travel</button>
    <button class="filter-btn" onclick="filterPosters('term')">🛡️ Term Life</button>
  </div>

  <!-- POSTERS GRID -->
  <div class="posters-grid" id="postersGrid">
    {% for poster in posters %}
    <div class="poster-card" data-category="{{ poster.category_id }}">
      <div class="poster-preview {{ poster.color }}">
        <div class="poster-icon">{{ poster.icon }}</div>
        <div class="poster-card-id">#{{ poster.id }}</div>
      </div>
      <div class="poster-card-content">
        <div class="poster-category">{{ poster.category }}</div>
        <div class="poster-title">{{ poster.title }}</div>
        <div class="poster-style">{{ poster.style }} style</div>
        <div class="poster-tool">⚡ {{ poster.tool }}</div>
        <div class="poster-actions">
          <button class="btn btn-primary" onclick="showPoster({{ poster.id }})">View</button>
          <button class="btn btn-secondary" onclick="copyPrompt({{ poster.id }})">Copy</button>
        </div>
      </div>
    </div>
    {% endfor %}
  </div>

  <!-- FOOTER -->
  <div class="footer">
    <h3>Need Help? 🤝</h3>
    <p>{{ rm_name }} | PB Partners</p>
    <a href="tel:{{ rm_phone }}" class="contact">📞 {{ rm_phone }}</a>
  </div>

</div>

<!-- MODAL -->
<div class="modal" id="posterModal">
  <div class="modal-content">
    <button class="modal-close" onclick="closeModal()">✕</button>
    <div id="modalBody"></div>
  </div>
</div>

<!-- TOAST -->
<div class="toast" id="toast">✅ Copied to clipboard!</div>

<script>
  // Posters data
  const POSTERS = {{ posters | tojson }};
  
  // Filter posters
  function filterPosters(category) {
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    event.target.classList.add('active');
    
    const cards = document.querySelectorAll('.poster-card');
    cards.forEach(card => {
      if (category === 'all' || card.dataset.category === category) {
        card.style.display = 'block';
      } else {
        card.style.display = 'none';
      }
    });
  }
  
  // Show poster details modal
  function showPoster(id) {
    const poster = POSTERS.find(p => p.id === id);
    if (!poster) return;
    
    document.getElementById('modalBody').innerHTML = `
      <h2 class="modal-title">${poster.icon} ${poster.title}</h2>
      <div class="modal-category">${poster.category} · ${poster.style} style</div>
      <div class="modal-tool">⚡ Best Tool: ${poster.tool}</div>
      
      <h4 style="margin-top: 14px; color: var(--pb-blue-dark); font-family: 'Fraunces', serif;">📋 AI Prompt:</h4>
      <div class="prompt-box" id="promptText">${poster.prompt}</div>
      
      <div class="modal-instructions">
        <h4>🚀 Quick Steps:</h4>
        <ol>
          <li><strong>Copy</strong> the prompt above (use Copy button)</li>
          <li>Open <strong>${poster.tool}</strong> ${getToolUrl(poster.tool)}</li>
          <li><strong>Paste</strong> the prompt and click Generate</li>
          <li>Image ready in 30 seconds!</li>
          <li>Add your name on photopea.com or Canva mobile</li>
          <li>Share on WhatsApp!</li>
        </ol>
      </div>
      
      <div class="modal-actions">
        <button class="btn btn-primary" onclick="copyPromptFromModal('${poster.id}')">📋 Copy Prompt</button>
        <button class="btn btn-secondary" onclick="openTool('${poster.tool}')">⚡ Open ${poster.tool}</button>
      </div>
    `;
    
    document.getElementById('posterModal').classList.add('active');
  }
  
  function getToolUrl(tool) {
    if (tool === 'Ideogram') return '(ideogram.ai)';
    if (tool === 'Microsoft Designer') return '(designer.microsoft.com)';
    return '(bing.com/create)';
  }
  
  function openTool(tool) {
    let url = 'https://ideogram.ai';
    if (tool === 'Microsoft Designer') url = 'https://designer.microsoft.com';
    if (tool === 'Bing Image Creator') url = 'https://bing.com/create';
    window.open(url, '_blank');
  }
  
  function copyPromptFromModal(id) {
    const poster = POSTERS.find(p => p.id == id);
    if (poster) {
      navigator.clipboard.writeText(poster.prompt);
      showToast('✅ Prompt copied! Now paste in ' + poster.tool);
    }
  }
  
  function copyPrompt(id) {
    const poster = POSTERS.find(p => p.id === id);
    if (poster) {
      navigator.clipboard.writeText(poster.prompt);
      showToast('✅ Copied! Open ' + poster.tool + ' to generate');
    }
  }
  
  function closeModal() {
    document.getElementById('posterModal').classList.remove('active');
  }
  
  function showToast(message) {
    const toast = document.getElementById('toast');
    toast.textContent = message;
    toast.classList.add('show');
    setTimeout(() => toast.classList.remove('show'), 3000);
  }
  
  // Close modal on outside click
  document.getElementById('posterModal').addEventListener('click', (e) => {
    if (e.target.id === 'posterModal') closeModal();
  });
</script>

</body>
</html>"""
