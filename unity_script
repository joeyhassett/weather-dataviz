using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;

[RequireComponent(typeof(ParticleSystem))]
public class ReadCSV : MonoBehaviour
{
    private ParticleSystemRenderer psRenderer;
    public Vector3 newPosition;
    // Start is called before the first frame update
    void Start()
    {
        // calling function
        ParticleSystem ps = GetComponent<ParticleSystem>();
        ParticleSystem.CollisionModule collisionModule = GetComponent<ParticleSystem>().collision;
        ParticleSystem.VelocityOverLifetimeModule velocityModule = GetComponent<ParticleSystem>().velocityOverLifetime;
        ParticleSystem.MainModule mainModule = GetComponent<ParticleSystem>().main;
        ParticleSystemRenderer renderer = GetComponent<ParticleSystem>().GetComponent<ParticleSystemRenderer>();
        ParticleSystem.MainModule main_ss = ps.main;

        var main = ps.main;
        var sh = ps.shape;
        var coll = ps.collision;
        var em = ps.emission;

        main.duration = 10f;
        main.startLifetime = 1f;
        main.startDelay = 0f;
        main.startColor = new Color(255f,255f,255f,125f);
        main.maxParticles = 100000;
        GetComponent<ParticleSystem>().transform.position = newPosition;
        sh.shapeType = ParticleSystemShapeType.Box;
        sh.scale = new Vector3(200f, 1f, 180f);
        coll.type = ParticleSystemCollisionType.World;
        collisionModule.enabled = true;
        coll.bounce = 0f;
        coll.dampen = 1f;
        velocityModule.enabled = true;
        velocityModule.space = ParticleSystemSimulationSpace.World;
        velocityModule.x = new ParticleSystem.MinMaxCurve(0, 0);
        velocityModule.y = new ParticleSystem.MinMaxCurve(-35, -25);
        velocityModule.z = new ParticleSystem.MinMaxCurve(0, 0);
        mainModule.startSpeed = 0f;
        renderer.renderMode = ParticleSystemRenderMode.Stretch;
    

        

        // reading file from location
        StreamReader strReader = new StreamReader("/Users/ant/Downloads/AImmerseGT/weatherdata.csv");
        // bool endOfFile = false;
        string data_String = strReader.ReadLine();
        var data_values = data_String.Split (',');
        var day = data_values[0].ToString();
        // var weather = data_values[1].ToString();
        var weather = "Drizzle"; 
        var windy_bool = false;
        if ((int.Parse(data_values[2])) == 1){
            windy_bool = true;
        }
        
        Debug.Log(day);
        Debug.Log(weather);
        Debug.Log(windy_bool);


        if (weather == "Rain") {
            Terrain terrain = Terrain.activeTerrain;
            TerrainLayer grassLayer = terrain.terrainData.terrainLayers[0];
            TerrainLayer snowLayer = terrain.terrainData.terrainLayers[1];
            TerrainLayer[] layers = new TerrainLayer[2] {grassLayer, snowLayer};
            terrain.terrainData.terrainLayers = layers;
            main_ss.startSize3D = true;
            main_ss.startSizeXMultiplier = .1f;
            main_ss.startSizeYMultiplier = 1.5f;
            main_ss.startSizeZMultiplier = .1f;
            em.rateOverTime = 10000f;
        } 
        else if (weather == "Drizzle") {
            Terrain terrain = Terrain.activeTerrain;
            TerrainLayer grassLayer = terrain.terrainData.terrainLayers[0];
            TerrainLayer snowLayer = terrain.terrainData.terrainLayers[1];
            TerrainLayer[] layers = new TerrainLayer[2] {grassLayer, snowLayer};
            terrain.terrainData.terrainLayers = layers;
            main_ss.startSize3D = true;
            main_ss.startSizeXMultiplier = .1f;
            main_ss.startSizeYMultiplier = 1.5f;
            main_ss.startSizeZMultiplier = .1f;
            em.rateOverTime = 5000f;
        } else if (weather == "Snow") {   
            Terrain terrain = Terrain.activeTerrain;
            TerrainLayer grassLayer = terrain.terrainData.terrainLayers[0];
            TerrainLayer snowLayer = terrain.terrainData.terrainLayers[1];
            TerrainLayer[] layers = new TerrainLayer[2] {snowLayer, grassLayer};
            terrain.terrainData.terrainLayers = layers;
            main_ss.startSize3D = true;
            main_ss.startSizeXMultiplier = .5f;
            main_ss.startSizeYMultiplier = .5f;
            main_ss.startSizeZMultiplier = .5f;
            em.rateOverTime = 1000f;
        }
        // else if (weather == "Thunderstorm") {

        // } 
        
        // else if (weather == "Cloudy") {

        // } else if (weather == "Clear Skies") {

        // }
    }
}
