export default async function handler(req, res) {
  const { fingerprint } = req.query;

  if (!fingerprint) {
    return res.status(400).json({ error: 'Missing fingerprint parameter' });
  }

  const targetUrl = `https://script.google.com/macros/s/AKfycbwh0pjeBbTr27VFTtpWUpKdDdU-T3FGGBZzVXVaZmj21OeouoZ5LkhK8vfjNPbYMUmP/exec?fingerprint=${encodeURIComponent(fingerprint)}`;

  try {
    const response = await fetch(targetUrl);
    const text = await response.text();
    res.status(200).send(text);
  } catch (err) {
    res.status(500).json({ error: 'Proxy request failed', details: err.message });
  }
}
