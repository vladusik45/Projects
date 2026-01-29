
using Microsoft.AspNetCore.Authentication;

var builder = WebApplication.CreateBuilder();

builder.Services.AddDistributedMemoryCache();
builder.Services.AddSession();

var app = builder.Build();

app.UseSession();


app.MapGet("/form", async (HttpContext context) =>
{
    context.Response.ContentType = "text/html; charset=utf-8";
    string form = @"<!DOCTYPE html>
    <html>
    <head>
        <meta charset='utf-8' />
        <title>Test form</title>
        <style>
            body {
                background: grey;
                color: white;
                border-radius: 1em;
                padding: 1em;
                position: absolute;
                top: 50%;
                left: 50%;
                margin-right: -50%;
                transform: translate(-50%, -50%) }
        </style>
    </head>
    <body>
        <h1>Example</h1>
        <form method='post'>
            <p>
                <label>Enter any message</label><br />
                <input name='anymes' />
            </p>
            <input type='submit' value='Set value' />
        </form>
    </body>
    </html>";
    await context.Response.WriteAsync(form);
});

app.MapPost("/form", async (string? returnUrl, HttpContext context) =>
{
    var form = context.Request.Form;
    string anyMes = form["anymes"];
    context.Session.SetString("anymes", anyMes + " from session");

    context.Response.Cookies.Append("anymess", anyMes + " from cookies");

    return Results.Redirect("/new");
});

app.Map("/new", (HttpContext context) =>
{
    string? anyMesCookie = context.Request.Cookies["anymess"];
    return $"\n\n\t\tHello! Your message was \"{context.Session.GetString("anymes")}\" or \"{anyMesCookie}\".";
});


app.Run();