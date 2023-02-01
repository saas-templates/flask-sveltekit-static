# Flask + Svelte

This project sample shows how to use SvelteKit frontend with Flask backend.

## Key Points to note

Flask does not automatically translate `/a` into `/a/index.html` even if an `index.html` file exists. Due to this, it's necessary to build the sveltekit as a pure SPA:

Before following these steps, please note:

1. A proper web server (e.g., nginx) is better suited at serving static files.
2. By using SvelteKit in pure SPA mode, you will lose the advantages of pre-rendering (less client-side overhead, less-dependency on javascript, better SEO, etc.) 

### Steps

1. Add these to your `src/routes/+layout.ts` or `src/routes/+layout.js` file.
   
   ```ts
   export const ssr = false;
   export const prerender = false;
   ```

2. Set kit options as shown below (in `svelte.config.js`):

   ```js
   {
       kit: {
           prerender: { entries: [] }, // disable prerender
           adapter: adapter({
               fallback: "index.html",
           }),
       },
   }
   ```

3. In your flask file, add the following routes:

   ```python
   @app.route("/")
   def index_route():
       return send_from_directory('./build', 'index.html')

   @app.route("/<path:path>")
   def static_files(path):
       return send_from_directory('./build', path)
   ```

