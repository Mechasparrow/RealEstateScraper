Sure, here is the revised README for your project:

# Real Estate Property Scraper

This project is a RESTful API that provides access to real estate data from Minnesota. The API is built on FastAPI, a modern Python framework for building APIs.

## Purpose

The purpose of this project is to provide a way for people to keep up to date with real estate in Minnesota. The data can be used to track prices, find new listings, and research neighborhoods.

## Target Audience

The target audience for this project is anyone who is interested in real estate in Minnesota. This includes home buyers, sellers, investors, and renters.

## Key Features

The key features of this project are:

* The ability to retrieve real estate data from the Minnesota Multiple Listing Service (MLS).
* The ability to paginate the results.
* The ability to search by search ID.

## How to Install and Use

To install this project, you will need to have Python 3 installed. Once you have Python installed, you can install the project dependencies by running the following command:

```
pip install -r requirements.txt
```

Once the dependencies are installed, you can start the server by running the following command:

```
python -m uvicorn server:app
```

The server will start on port 8000. You can access the API documentation by opening the following URL in your browser:

```
http://localhost:8000/docs
```

## Known Limitations

This project is still under development, so there are a few known limitations:

* The data is not always up to date.
* The API is not yet fully documented.

## Getting Help

If you have any questions or problems, please create a GitHub issue.

## API Endpoints

The following are the API endpoints that are currently available:

* `/paginated-properties`

This endpoint returns a paginated list of properties. The pagination parameters are `page` and `size`. The default values for `page` and `size` are 1 and 10, respectively.

* `/properties`

This endpoint returns a list of all properties. The results are not paginated.

* `/scrape`

This endpoint scrapes the MLS for new properties. The search ID must be specified in the request body.

## Request Bodies

The following request bodies are currently supported:

* `Pagination`

This request body is used to paginate the results of the `/paginated-properties` endpoint. The request body has the following properties:

    * `page`: The page number.
    * `size`: The number of properties per page.

* `SearchId`

This request body is used to scrape the MLS for new properties. The request body has the following property:

    * `search_id`: The search ID.

## Response Bodies

The following response bodies are currently supported:

* `Property`

This response body represents a property. The response body has the following properties:

    * `id`: The property ID.
    * `address`: The property address.
    * `city`: The property city.
    * `state`: The property state.
    * `zip_code`: The property zip code.
    * `price`: The property price.
    * `beds`: The number of bedrooms.
    * `baths`: The number of bathrooms.
    * `square_feet`: The property square footage.
    * `lot_size`: The property lot size.
    * `status`: The property status.
    * `created_at`: The date and time the property was created.
    * `updated_at`: The date and time the property was updated.

* `HTTPValidationError`

This response body is returned if the request body is invalid. The response body has the following properties:

    * `detail`: An array of validation errors.

I hope this helps!