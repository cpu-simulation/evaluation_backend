Frontend of Evaluation Project

### Install
First go the frontend directory and run this command to install packages:

```
npm install
```

### Build
For building the frontend, use the command below:

```
npm run build
```

This will put the production ready build, in `dist` directory so you can use it by serving
`dist/index.html`. Note that you should make `dist`, a public directory so users can access its contents.
The website won't be available if you just pass the html, while users don't have access to styles and scripts.

One example is in `index.js` file.

You can change the output directory by heading to `vite.config.ts` too.

### Exploring the UI
You can explore the UI by running the MockAPI using this commands: (server will serve built files too)
```
npm run server
```

### Debugging
You can run frontend in dev mode using the command below, just make sure to adjust server address in `vite.config.ts` and its `proxy` option:
```
npm run dev
```
