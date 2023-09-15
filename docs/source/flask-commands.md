# Flask Commands

The extension also provides a couple of new Flask commands that use Rich to show information in the console.

Every command is toggleable, so you can disable them by setting the corresponding configuration variable to {py:data}`False`. For example, to disable the `rich-routes` command, set `RICH_ROUTES` to {py:data}`False`.

- `rich-routes`: Show all routes in the app with {doc}`rich:tables`.