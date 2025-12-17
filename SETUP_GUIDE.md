# Karobwa Website Module - Setup & Fixes

## Issues Fixed

### 1. **Blank White Screen / Missing Slider Display**

**Problem:** The website was showing a blank white screen instead of the slider.

**Causes:**
- Route mapping issue: Homepage was not properly routed to the Karobwa homepage template
- Missing static image files referenced in the template

**Solutions Implemented:**
- ✅ Added default homepage route (`/`) in `controllers/main.py` that renders the karobwa homepage
- ✅ Created static directory structure: `/static/src/img/`
- ✅ Added placeholder slider images: `slider-13.jpg`, `slider-14.jpg`, `slider-15.jpg`

### 2. **Password Required for Odoo Restart**

**Problem:** Every Odoo restart required entering the sudo password manually.

**Solution:**
- ✅ Created passwordless restart script: `/opt/odoo/custom-addons/restart-odoo.sh`
- ✅ Added sudoers entry in `/etc/sudoers.d/odoo-restart` allowing passwordless execution
- ✅ Script properly activates virtual environment before running Odoo

## How to Use

### Quick Restart (No Password Required)

```bash
sudo /opt/odoo/custom-addons/restart-odoo.sh
```

This command will:
1. Stop any running Odoo processes
2. Activate the Python virtual environment
3. Restart Odoo with the `karobwa_website` module update
4. Stop after initialization completes

### Testing the Website

1. Ensure Odoo is running on `http://localhost:8069`
2. Visit the homepage: `http://localhost:8069` or `http://localhost:8069/karobwa_scents`
3. You should see:
   - A full-screen slider with fade transition
   - 4 product slides with images and text
   - A scrolling marquee section below
   - Pagination dots for navigation

## File Structure

```
karobwa_website/
├── __init__.py
├── __manifest__.py
├── controllers/
│   ├── __init__.py
│   └── main.py (UPDATED - added default home route)
├── views/
│   ├── home.xml
│   └── website_templates.xml
├── static/
│   └── src/
│       └── img/
│           ├── slider-13.jpg (NEW)
│           ├── slider-14.jpg (NEW)
│           └── slider-15.jpg (NEW)
└── restart-odoo.sh (NEW - passwordless restart script)
```

## Module Configuration

- **Default route**: `/` → Homepage with slider
- **Custom route**: `/karobwa_scents` → Same homepage
- **About route**: `/karobwa_scents/about` → About page
- **Port**: 8069 (configurable in `/etc/odoo.conf`)

## Next Steps (Optional Improvements)

1. **Replace placeholder images**: Update the SVG images in `/static/src/img/` with actual product photography
2. **Add more content**: Extend the homepage with product catalog sections
3. **Customize styling**: Modify CSS in `home.xml` for brand colors
4. **Add dynamic data**: Connect to Odoo models for products and categories

## Troubleshooting

If the slider still doesn't display:

1. **Clear browser cache**: Press `Ctrl+Shift+Delete` (Chrome) or `Cmd+Shift+Delete` (Mac)
2. **Check module status**: Ensure `karobwa_website` is installed in Apps
3. **View browser console**: Press `F12` and check the Console tab for JavaScript errors
4. **Check Odoo logs**: Look for any Python errors in `/var/log/odoo/`

## Sudo Configuration

The passwordless restart is configured in `/etc/sudoers.d/odoo-restart`:
- User: `oluwa`
- Commands: 
  - `/opt/odoo/custom-addons/restart-odoo.sh`
  - `/usr/bin/pkill`

To modify permissions in the future, edit the sudoers file with:
```bash
sudo visudo -f /etc/sudoers.d/odoo-restart
```
