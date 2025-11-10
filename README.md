# Crawford County Department of Job & Family Services Website

Official website for Crawford County DJFS providing information about public assistance, child support, child and adult protective services, and workforce development.

## Features

- Responsive design using USWDS (U.S. Web Design System)
- Public assistance services information
- Child support services
- Child & adult protective services
- OhioMeansJobs integration
- Interactive chat widget
- Mobile-friendly navigation

## Deployment

This site is configured for deployment on Railway.

### Railway Deployment

1. Connect your GitHub repository to Railway
2. Railway will automatically detect the Node.js application
3. The site will be served using Express on the configured PORT

### Local Development

To run locally:

```bash
npm install
npm start
```

Visit `http://localhost:3000` to view the site.

## Project Structure

```
├── belmontjfs copy/       # Main website files
│   ├── index.html         # Homepage
│   ├── styles.css         # Custom styles
│   ├── public/            # Images and assets
│   └── ...
├── crawfordcountyjfs.org/ # Content and documentation
├── server.js              # Express server for deployment
└── package.json           # Node.js dependencies
```

## Technologies

- HTML5
- CSS3
- JavaScript
- USWDS 3.7.1
- Font Awesome 6.4.0
- Express.js (for serving)

## License

Copyright © 2025 Crawford County Department of Job & Family Services. All rights reserved.
