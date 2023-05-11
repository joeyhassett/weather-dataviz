using System;
using System.Collections;
using System.Collections.Generic;
using System.Threading.Tasks;
using UnityEngine;


using TMPro;
using UnityEngine.UI;
using UnityEngine.Networking;
using Newtonsoft.Json;

public class GetWeatherData : MonoBehaviour
{
    private string requestUrl = "https://maps.googleapis.com/maps/api/geocode/json";
    private string geocode_apikey = "AIzaSyB8atCJJPW1nddKKHS4XWwuHKRaHbJ-llU";
    private string wb_apikey = "8660093900b24664a3d30561337fc1de";
    private string lat;
    private string lng;
    public static string address = "Atlanta, GA";
    public string day = "0";
    public Slider slider;
    public TMP_Dropdown dropdown;
    public TextMeshProUGUI sliderText;
    public TextMeshProUGUI buttonText;

    // Update is called once per frames
    void Start()
    {
        GameObject.Find("Update").GetComponent<Button>().onClick.AddListener(GetData);
    }

    public void Update()
    {
        sliderText.text = slider.value.ToString("0");
        day = slider.value.ToString("0");
    }

    public void setAddress(int val)
    {
        if (val == 0)
        {
            address = "Atlanta, GA";
        }
        else if (val == 1)
        {
            address = "New York City, NY";
        }
    }

    void GetData() => StartCoroutine(GetData_Coroutine());

    IEnumerator GetData_Coroutine()
    {
        using (UnityWebRequest request = UnityWebRequest.Get($"{requestUrl}?address={address}&key={geocode_apikey}"))
        {
            yield return request.SendWebRequest();
            if (request.isNetworkError || request.isHttpError)
            {
                buttonText.text = request.error;
            }
            else
            {
                string json = request.downloadHandler.text;
                string searchSubstring = "location";
                string[] lines = json.Split("\n");
                for (int i=0; i<lines.Length; i++)
                {
                    if (lines[i].Contains(searchSubstring)){
                        char[] characters_lat = lines[i + 1].ToCharArray();
                        char[] characters_lng = lines[i + 2].ToCharArray();
                        string lat_str = "";
                        string lng_str = "";
                        foreach (char c in characters_lat)
                        {
                            if (char.IsDigit(c) || c == '.' || c == '-')
                            {
                                lat_str += c.ToString();
                            }
                        }
                        lat = lat_str;
                        foreach (char c in characters_lng)
                        {
                            if (char.IsDigit(c) || c == '.' || c == '-')
                            {
                                lng_str += c.ToString();
                            }
                        }
                        lng = lng_str;
                        break;
                    }
                }
            }
        }
        using (UnityWebRequest request = UnityWebRequest.Get($"https://api.weatherbit.io/v2.0/forecast/daily?lat={lat}&lon={lng}&key={wb_apikey}"))
        {
            yield return request.SendWebRequest();
            if (request.isNetworkError || request.isHttpError)
            {
                buttonText.text = request.error;
            }
            else
            {
                string json = request.downloadHandler.text;
                json_data myData = JsonUtility.FromJson<json_data>(json);
                buttonText.text = $"{myData.data[int.Parse(day)].clouds} and {myData.city_name}";
            }
        }
    }
}


[System.Serializable]
public class json_data
{
    public string city_name;
    public string country_code;
    public DailyWeatherData[] data;
    public string lat;
    public string lon;
    public string state_code;
    public string timezone;
}

[System.Serializable]
public class DailyWeatherData
{
    public string app_max_temp;
    public string app_min_temp;
    public string clouds;
    public string clouds_hi;
    public string clouds_low;
    public string clouds_mid;
    public string datetime;
    public string dewpt;
    public string high_temp;
    public string low_temp;
    public string max_dhi;
    public string max_temp;
    public string min_temp;
    public string moon_phase;
    public string moon_phase_lunation;
    public string moonrise_ts;
    public string moonset_ts;
    public string ozone;
    public string pop;
    public string precip;
    public string pres;
    public string rh;
    public string slp;
    public string snow;
    public string snow_depth;
    public string sunrise_ts;
    public string sunset_ts;
    public string temp;
    public string ts;
    public string uv;
    public string valid_date;
    public string vis;
    public string wind_cdir;
    public string wind_cdir_full;
    public string wind_dir;
    public string wind_gust_spd;
    public string wind_spd;
}
