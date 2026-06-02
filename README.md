# MailSense

**Make sense of your inbox.**  
MailSense is an intelligent application for email analysis and management. Using natural language processing (NLP) techniques, it automatically categorizes messages, extracts insights, and provides analytical views of your email activity.

---

## Overview

MailSense addresses the challenge of information overload in professional inboxes by offering:

- Automatic email classification by category and priority
- Extraction of summaries and action items from messages
- Analytics dashboard to monitor trends and volumes
- Modern, fully responsive user interface
- Modular architecture, easily extensible

---

## Tech Stack

| Component | Technology |
|-----------|------------|
| Frontend | React 18, TypeScript, TailwindCSS |
| State Management | Zustand, React Query |
| Backend | Node.js, Express |
| NLP / AI | OpenAI API, Transformers.js |
| Database | PostgreSQL |
| Email Protocol | IMAP/SMTP (node-imap), Gmail API (OAuth 2.0) |
| Tooling | Vite, ESLint, Prettier, Vitest |

---

## Prerequisites

Before you begin, ensure you have installed:

- Node.js >= 18
- npm or pnpm
- (Optional) OpenAI API key for advanced AI features

---

## Installation

```bash
git clone https://github.com/fabio-cerundolo/MailSense.git
cd MailSense

npm install
```

## Configuration

Create a `.env` file from the provided template:

```bash
cp .env.example .env
```

Fill in the environment variables with your values:

```env
VITE_API_URL=http://localhost:3000
OPENAI_API_KEY=sk-...
GMAIL_CLIENT_ID=...
GMAIL_CLIENT_SECRET=...
```

## Usage

Start the development server:

```bash
npm run dev        # Frontend
npm run server     # Backend
```

The application will be available at [http://localhost:5173](http://localhost:5173).

---

## Build

```bash
npm run build       # Production build
npm run preview     # Preview production build
```

## Testing

```bash
npm test            # Unit tests
npm run test:e2e    # End-to-end tests
```

---

## Project Structure

```
MailSense/
├── src/
│   ├── components/     # Reusable UI components
│   ├── pages/          # Application pages
│   ├── hooks/          # Custom hooks
│   ├── services/       # API services and email integration
│   ├── utils/          # Utility functions
│   └── types/          # TypeScript definitions
├── server/             # Node.js backend
├── public/             # Static assets
└── docs/               # Documentation
```

---

## Roadmap

- [x] MVP with basic categorization
- [x] Gmail integration via OAuth 2.0
- [x] Analytics dashboard
- [ ] Multi-account support
- [ ] Outlook plugin
- [ ] Native mobile version (React Native)
- [ ] Offline processing with local models

---

## Contributing

Contributions are welcome. To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/feature-name`)
3. Commit your changes (`git commit -m 'feat: description'`)
4. Push to the branch (`git push origin feature/feature-name`)
5. Open a Pull Request

Please follow [Conventional Commits](https://www.conventionalcommits.org/) conventions for commit messages.

---

## License

Distributed under the MIT License. See [`LICENSE`](./LICENSE) for details.

---

## Author

**Fabio Cerundolo** — Full-Stack Developer

- Portfolio: [fabio-cerundolo.dev](https://fabio-cerundolo.dev)
- GitHub: [@fabio-cerundolo](https://github.com/fabio-cerundolo)
- LinkedIn: [fabio-cerundolo](https://linkedin.com/in/fabio-cerundolo)
