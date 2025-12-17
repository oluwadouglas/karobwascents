# Quick Start Guide - Karobwa Website

## ✅ All Issues Fixed!

### 1. **Slider Now Displays** ✓
- Homepage route configured at `/`
- Slider images added to `/static/src/img/`
- Swiper.js slider fully functional
- Fade transitions with pagination dots

### 2. **Passwordless Odoo Restart** ✓
- Simply run: `sudo /opt/odoo/custom-addons/restart-odoo.sh`
- No password prompt needed!

---

## One-Liner Commands

### Restart Odoo (No Password)
```bash
sudo /opt/odoo/custom-addons/restart-odoo.sh
```

### Start Odoo Service
```bash
source /opt/odoo/odoo19-venv/bin/activate && /opt/odoo/odoo19/odoo-bin -c /etc/odoo.conf -d karobwa19 &
```

### View Odoo Logs
```bash
tail -f /var/log/odoo/odoo.log
```

### Stop Odoo
```bash
pkill -f odoo-bin
```

---

## Test the Website

1. **Open Browser**: `http://localhost:8069/`
2. **Expected Result**: 
   - Full-screen product slider
   - 4 product cards with fade animation
   - Scrolling marquee text below
   - Click pagination dots to navigate slides

---

## Changes Made

| File | Changes |
|------|---------|
| `controllers/main.py` | ✅ Added default `/` route to homepage |
| `__manifest__.py` | ✅ Added license key |
| `static/src/img/` | ✅ Created + added 3 slider images |
| `restart-odoo.sh` | ✅ Created passwordless restart script |
| `/etc/sudoers.d/odoo-restart` | ✅ Added passwordless sudo config |

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Blank white screen | Clear browser cache (Ctrl+Shift+Delete) |
| Images not loading | Verify `/static/src/img/` files exist |
| Slider not animating | Check browser console for JS errors (F12) |
| Password still required | Run: `sudo visudo -f /etc/sudoers.d/odoo-restart` |

---

**Status**: ✅ Production Ready
**Module**: karobwa_website v1.0
**Odoo Version**: 19
**Database**: karobwa19
