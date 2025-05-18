using Microsoft.WindowsAPICodePack.Net;
using System;
using System.IO;
using Newtonsoft.Json;

public enum ToolKind
{
    Target,
    Save,
    Max
}
public class AppSettings
{
    public string TargetPath { get; set; } = @"C:";
    public string SavePath { get; set; } = @"C:";
}
