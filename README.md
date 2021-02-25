# BRIEF

The paginate function accepts the following parameters:

`totalItems (required)` - the total number of items to be paged
`currentPage (optional)` - the current active page, defaults to the first page
`pageSize (optional)` - the number of items per page, defaults to 10
`maxPages (optional)` - the maximum number of page navigation links to display, defaults to 10

The output of the paginate function is an object containing all the information needed to display the current page of items in the view and the page navigation links.