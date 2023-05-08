using System;
using Newtonsoft.Json;
using System.Net.Http;
using System.Threading.Tasks;

namespace MyNamespace
{
    public class Program
    {
        public static async Task Main()
        {
            string address = "20 W 34th St., New York, NY 10001";
            int day = 15;
            string wb_apikey = "8660093900b24664a3d30561337fc1de";
            string geocode_apikey = "AIzaSyB8atCJJPW1nddKKHS4XWwuHKRaHbJ-llU";
            string geocode_apiurl = "https://maps.googleapis.com/maps/api/geocode/json";

            using (HttpClient client = new HttpClient())
            {
                try
                {
                    string requestUrl = $"{geocode_apiurl}?address={Uri.EscapeDataString(address)}&key={geocode_apikey}";
                    HttpResponseMessage response_geocode = await client.GetAsync(requestUrl);
                    if (response_geocode.IsSuccessStatusCode)
                    {
                        string json_geocode = await response_geocode.Content.ReadAsStringAsync();
                        dynamic result_geocode = Newtonsoft.Json.JsonConvert.DeserializeObject(json_geocode);
                        string status = result_geocode.status;
                        if (status == "OK")
                        {
                            string lat = result_geocode.results[0].geometry.location.lat;
                            string lon = result_geocode.results[0].geometry.location.lng;
                            Console.WriteLine($"Latitude: {lat}, Longitude: {lon}");
                            HttpResponseMessage response = await client.GetAsync($"https://api.weatherbit.io/v2.0/forecast/daily?lat={lat}&lon={lon}&key={wb_apikey}");
                            string json_wb = await response.Content.ReadAsStringAsync();
                            dynamic result_wb = Newtonsoft.Json.JsonConvert.DeserializeObject(json_wb);
                            Console.WriteLine(result_wb.data[day].weather.description);

                            using (StreamWriter writer = new StreamWriter("coor")){
                                writer.WriteLine(lat);
                                writer.WriteLine(lon);
                            };
                            
                        }
                        else
                        {
                            Console.WriteLine($"Geocoding failed. Invalid address or API key.");
                        }
                    }
                    else
                    {
                        Console.WriteLine($"Request failed with status code: {response_geocode.StatusCode}");
                    }}
                catch (Exception ex)
                {
                    Console.WriteLine($"An error occured: {ex.Message}");
                }
            }
        }
    }
}