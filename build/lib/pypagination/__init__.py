import math
import json 

def paginate(totalItems, currentPage=1, pageSize=10, maxPages=10):
    # calculate total pages
    totalPages = math.ceil(totalItems / pageSize)

    # ensure current page isn't out of range
    if currentPage < 1:
        currentPage = 1
    elif currentPage > totalPages:
        currentPage = totalPages

    global startPage
    global endPage

    if totalPages <= maxPages:
        startPage = 1
        endPage = totalPages
    else: 
        maxPagesBeforeCurrentPage = math.floor(maxPages / 2)
        maxPagesAfterCurrentPage = math.ceil(maxPages / 2) - 1
        if currentPage <= maxPagesBeforeCurrentPage: 
            # current page near the start
            startPage = 1
            endPage = maxPages
        elif currentPage + maxPagesAfterCurrentPage >= totalPages:
            # current page near the end
            startPage = totalPages - maxPages + 1
            endPage = totalPages
        else:
            # current page somewhere in the middle
            startPage = currentPage - maxPagesBeforeCurrentPage
            endPage = currentPage + maxPagesAfterCurrentPage
    

    # calculate start and end item indexes
    startIndex = (currentPage - 1) * pageSize
    endIndex = min(startIndex + pageSize - 1, totalItems - 1)

    pages = []
    # create an array of pages to ng-repeat in the pager control
    for i in range(startPage, endPage+1):
        pages.append(i)
        
    # return object with all pager properties required by the view
    res = {}
    res['totalItems'] = int(totalItems)
    res['currentPage'] = int(currentPage)
    res['pageSize'] = int(pageSize)
    res['totalPages'] = int(totalPages)
    res['startPage'] = int(startPage)
    res['endPage'] = int(endPage)
    res['startIndex'] = int(startIndex)
    res['endIndex'] = int(endIndex)
    res['pages'] = pages

    return json.dumps(res)