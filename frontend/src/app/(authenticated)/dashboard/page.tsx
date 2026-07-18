"use client";

import React, { useState, useEffect, useRef } from "react";
import { 
  Cpu, Database, Network, Activity, Terminal, Shield
} from "lucide-react";
import { motion } from "framer-motion";
import CyberCard from "@/components/ui/CyberCard";
import CyberBadge from "@/components/ui/CyberBadge";
import { getDashboard, toggleEquipment } from "@/services/apiServices";

interface EquipmentItem {
  id: string;
  name: string;
  type: string;
  plant: string;
  status: "ONLINE" | "WARNING" | "OFFLINE";
  load: number;
}

export default function DashboardPage() {
  const [stats, setStats] = useState<any>(null);
  const statsRef = useRef<any>(null);
  // Telemetry status state
  const [chartData, setChartData] = useState<number[]>([45, 52, 48, 62, 58, 71, 65, 78, 72, 85, 80, 92, 88, 96, 90]);
  const [cpuTemp, setCpuTemp] = useState(42);
  const [systemLoad, setSystemLoad] = useState(74);
  const [bufferMem, setBufferMem] = useState(61);

  useEffect(() => {
    statsRef.current = stats;
  }, [stats]);

  useEffect(() => {
    const fetchDashboardStats = async () => {
      try {
        const res = await getDashboard();
        if (res && res.data) {
          setStats(res.data);
          if (res.data.cpuTemp) setCpuTemp(res.data.cpuTemp);
          if (res.data.bufferMem) setBufferMem(res.data.bufferMem);
          if (res.data.equipmentList) {
            const mappedList = res.data.equipmentList.map((eq: any) => ({
              id: eq._id,
              name: eq.name,
              type: eq.type,
              plant: eq.plant,
              status: eq.status,
              load: eq.load
            }));
            setEquipmentList(mappedList);
          }
        }
      } catch (error) {
        console.error("Dashboard stats fetch failed:", error);
      }
    };
    fetchDashboardStats();
    const statsInterval = setInterval(fetchDashboardStats, 5000);
    return () => clearInterval(statsInterval);
  }, []);

  // Equipment state
  const [equipmentList, setEquipmentList] = useState<EquipmentItem[]>([
    { id: "EQ-101", name: "Compressor C", type: "Rotary Screw", plant: "Sector A", status: "ONLINE", load: 68 },
    { id: "EQ-102", name: "Zone B Heat Exchanger", type: "Shell & Tube", plant: "Sector B", status: "WARNING", load: 82 },
    { id: "EQ-103", name: "Valve 04 Controller", type: "Flow Regulation", plant: "Sector B", status: "ONLINE", load: 45 },
    { id: "EQ-104", name: "Turbine Generator A", type: "Gas Turbine", plant: "Sector C", status: "OFFLINE", load: 0 },
  ]);

  // SCADA Sensor logs state
  const [scadaLogs, setScadaLogs] = useState<Array<{ id: number; prefix: string; text: string; status: "success" | "warning" | "error" | "info" | "primary" }>>([
    { id: 1, prefix: "OK", text: "Initializing Core microcode hypervisor v2.4...", status: "success" },
    { id: 2, prefix: "OK", text: "Allocating 32GB neural workspace buffer segments...", status: "success" },
    { id: 3, prefix: "INFO", text: "Latent WebSocket handshake: 18ms (Secure)", status: "info" },
    { id: 4, prefix: "OK", text: "Neo4j database connection established (82,000 nodes)", status: "success" },
    { id: 5, prefix: "WARN", text: "Zone B Heat Exchanger Temp: 81°C (Approaching limit)", status: "warning" },
  ]);
  const scadaContainerRef = useRef<HTMLDivElement>(null);

  // Telemetry dynamic loops
  useEffect(() => {
    const chartInterval = setInterval(() => {
      let avgLoad = 0;
      setEquipmentList(currentEq => {
        const active = currentEq.filter(e => e.status !== "OFFLINE");
        avgLoad = active.length > 0 
          ? Math.round(active.reduce((acc, e) => acc + e.load, 0) / active.length)
          : 0;

        const baseLoad = statsRef.current && statsRef.current.neuralCoreLoad ? statsRef.current.neuralCoreLoad : avgLoad;
        setSystemLoad(Math.min(100, Math.max(10, baseLoad + Math.floor(Math.random() * 6) - 3)));
        const baseTemp = statsRef.current && statsRef.current.cpuTemp ? statsRef.current.cpuTemp : 42;
        setCpuTemp(Math.min(95, Math.max(30, baseTemp + Math.floor(Math.random() * 4) - 2)));
        
        return currentEq.map(e => {
          if (e.status === "ONLINE") {
            const change = Math.floor(Math.random() * 5) - 2;
            return { ...e, load: Math.min(85, Math.max(40, e.load + change)) };
          } else if (e.status === "WARNING") {
            const change = Math.floor(Math.random() * 7) - 3;
            return { ...e, load: Math.min(95, Math.max(75, e.load + change)) };
          }
          return e;
        });
      });

      setChartData((prev) => {
        const next = [...prev.slice(1)];
        const last = next[next.length - 1];
        const delta = avgLoad - last;
        const change = Math.round(delta * 0.25) + (Math.floor(Math.random() * 9) - 4);
        const newVal = Math.min(100, Math.max(15, last + change));
        next.push(newVal);
        return next;
      });

      setBufferMem((prev) => {
        const change = Math.floor(Math.random() * 3) - 1;
        return Math.min(90, Math.max(45, prev + change));
      });
    }, 1000);

    return () => clearInterval(chartInterval);
  }, []);

  // SCADA console logger simulator loop
  useEffect(() => {
    const logInterval = setInterval(() => {
      const logTemplates = [
        { prefix: "OK", text: "SCADA WebSocket frame verified successfully.", status: "success" },
        { prefix: "INFO", text: "Neo4j query latency: 14ms (Nodes: 82,000)", status: "info" },
        { prefix: "WARN", text: "Zone B Heat Exchanger Temp: 81.4°C (Coolant throughput critical)", status: "warning" },
        { prefix: "OK", text: "ASTM compliance checklist validator returned status code 200.", status: "success" },
        { prefix: "FAIL", text: "Zone C regulator reports packet latency spikes (Restored)", status: "error" },
        { prefix: "OK", text: "SSL Tunnel handshake successfully completed.", status: "success" },
      ] as const;

      const randomTemplate = logTemplates[Math.floor(Math.random() * logTemplates.length)];
      setScadaLogs((prev) => {
        const next = [...prev];
        if (next.length > 20) next.shift();
        next.push({
          id: Date.now() + Math.random(),
          prefix: randomTemplate.prefix,
          text: randomTemplate.text,
          status: randomTemplate.status,
        });
        return next;
      });
    }, 3000);

    return () => clearInterval(logInterval);
  }, []);

  // Scroll to bottom helper for SCADA terminal
  useEffect(() => {
    if (scadaContainerRef.current) {
      scadaContainerRef.current.scrollTop = scadaContainerRef.current.scrollHeight;
    }
  }, [scadaLogs]);

  // SVG Chart path generators
  const points = chartData.map((val, idx) => `${idx * 21.4},${100 - val}`).join(" L ");
  const pathD = `M ${points}`;
  const areaD = `${pathD} L 300 100 L 0 100 Z`;

  // Toggle machinery health status controls
  const handleToggleEquipment = async (id: string, name: string) => {
    try {
      const res = await toggleEquipment(id);
      if (res && res.data) {
        const updated = res.data;
        const isTurningOn = updated.status === "ONLINE";
        
        setScadaLogs(logs => [
          ...logs,
          {
            id: Date.now(),
            prefix: isTurningOn ? "OK" : "WARN",
            text: `${name} has been switched ${updated.status}. Adjusting SCADA telemetry parameters...`,
            status: isTurningOn ? "success" : "warning"
          }
        ]);

        setEquipmentList(prev => prev.map(eq => 
          eq.id === id ? { ...eq, status: updated.status, load: updated.load } : eq
        ));
      }
    } catch (error) {
      console.error("Failed to toggle equipment status:", error);
    }
  };

  return (
    <div className="flex flex-col gap-6 select-none font-mono">
      
      {/* 1. TOP METRICS CARDS ROW */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        
        {/* Widget 1: System Load */}
        <CyberCard className="p-4!" showGrid={false} showBrackets={true}>
          <div className="flex items-center justify-between text-[10px] text-brand-text-secondary">
            <span>NEURAL CORE LOAD</span>
            <Activity className="h-4 w-4 text-brand-primary animate-pulse" />
          </div>
          <div className="flex items-baseline justify-between mt-2">
            <span className="text-2xl font-bold text-brand-text-primary tracking-tight">{systemLoad}%</span>
            <span className="text-[9px] text-brand-success font-semibold">OPTIMAL</span>
          </div>
          <div className="h-1 bg-brand-bg rounded-full mt-3 overflow-hidden">
            <div className="h-full bg-brand-primary rounded-full transition-all duration-300" style={{ width: `${systemLoad}%` }} />
          </div>
        </CyberCard>

        {/* Widget 2: Indexed Documents */}
        <CyberCard className="p-4!" showGrid={false} showBrackets={true}>
          <div className="flex items-center justify-between text-[10px] text-brand-text-secondary">
            <span>INDEXED DOCUMENTS</span>
            <Database className="h-4 w-4 text-brand-secondary" />
          </div>
          <div className="flex items-baseline justify-between mt-2">
            <span className="text-2xl font-bold text-brand-text-primary tracking-tight">
              {stats ? stats.totalDocuments : 3}
            </span>
            <span className="text-[9px] text-brand-text-secondary">ACTIVE INDICES</span>
          </div>
          <div className="h-1 bg-brand-bg rounded-full mt-3 overflow-hidden">
            <div className="h-full bg-brand-secondary rounded-full w-full" style={{ width: stats && stats.totalDocuments > 0 ? "100%" : "30%" }} />
          </div>
        </CyberCard>

        {/* Widget 3: CPU Temperature */}
        <CyberCard className="p-4!" showGrid={false} showBrackets={true}>
          <div className="flex items-center justify-between text-[10px] text-brand-text-secondary">
            <span>CORE COEF TEMP</span>
            <Cpu className="h-4 w-4 text-brand-warning" />
          </div>
          <div className="flex items-baseline justify-between mt-2">
            <span className="text-2xl font-bold text-brand-text-primary tracking-tight">{cpuTemp}°C</span>
            <span className={`text-[9px] font-bold ${cpuTemp > 75 ? "text-brand-danger animate-pulse" : "text-brand-warning"}`}>
              {cpuTemp > 75 ? "CRITICAL" : "STABLE"}
            </span>
          </div>
          <div className="h-1 bg-brand-bg rounded-full mt-3 overflow-hidden">
            <div className="h-full bg-brand-warning rounded-full transition-all duration-300" style={{ width: `${(cpuTemp / 95) * 100}%` }} />
          </div>
        </CyberCard>

        {/* Widget 4: Neo4j Graph Links */}
        <CyberCard className="p-4!" showGrid={false} showBrackets={true}>
          <div className="flex items-center justify-between text-[10px] text-brand-text-secondary">
            <span>KNOWLEDGE CONNECTIONS</span>
            <Network className="h-4 w-4 text-brand-success" />
          </div>
          <div className="flex items-baseline justify-between mt-2">
            <span className="text-2xl font-bold text-brand-text-primary tracking-tight">
              {stats ? (stats.graphNodesCount + stats.graphEdgesCount).toLocaleString() : "82,000"}
            </span>
            <span className={`text-[9px] font-bold ${stats?.aiServiceStatus === "OFFLINE" ? "text-brand-danger" : "text-brand-success"}`}>
              {stats ? stats.aiServiceStatus : "SYNCED"}
            </span>
          </div>
          <div className="h-1 bg-brand-bg rounded-full mt-3 overflow-hidden">
            <div className="h-full bg-brand-success rounded-full w-full" />
          </div>
        </CyberCard>

      </div>

      {/* 2. CORE SYSTEM OVERVIEW AND TELEMETRY GRID */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">

        {/* Real-time Line Graph Telemetry (col-span-7) */}
        <div id="telemetry" className="lg:col-span-7">
          <CyberCard 
            title="SCADA Real-Time Operations Telemetry" 
            subtitle="Fluctuations and load signals monitor"
            headerAction={
              <div className="flex items-center gap-2">
                <span className="w-2 h-2 rounded-full bg-brand-primary animate-pulse" />
                <span className="text-[10px] text-brand-primary font-bold">MONITORING</span>
              </div>
            }
          >
            <div className="w-full h-56 mt-2 relative flex flex-col justify-end">
              <div className="absolute inset-0 flex flex-col justify-between pointer-events-none opacity-20 z-0 text-[8px]">
                <div className="w-full border-t border-brand-primary/10 text-right pr-2 pt-0.5">100%</div>
                <div className="w-full border-t border-brand-primary/10 text-right pr-2 pt-0.5">75%</div>
                <div className="w-full border-t border-brand-primary/10 text-right pr-2 pt-0.5">50%</div>
                <div className="w-full border-t border-brand-primary/10 text-right pr-2 pt-0.5">25%</div>
                <div className="w-full border-t border-brand-primary/10" />
              </div>

              <svg viewBox="0 0 300 100" className="w-full h-full relative z-10 overflow-visible" preserveAspectRatio="none">
                <path d={areaD} className="fill-[url(#areaGrad)] stroke-none transition-all duration-300" />
                <path d={pathD} className="fill-none stroke-brand-primary stroke-[1.5] transition-all duration-300" />
              </svg>
            </div>

            <div className="border-t border-brand-primary/10 pt-3 mt-3 flex items-center justify-between text-[9px] text-brand-text-secondary">
              <span>SAMPLING_INTERVAL: 1.0s</span>
              <span>BUFFER_MAX: 15 POINTS</span>
              <span>FREQUENCY: 5.2 GHz</span>
            </div>
          </CyberCard>
        </div>

        {/* Equipment Status Overview Grid (col-span-5) */}
        <div className="lg:col-span-5">
          <CyberCard 
            title="Equipment Overview & Operational Control" 
            subtitle="Live plant machinery monitor status and hyperdrive loads"
          >
            <div className="flex flex-col gap-3 mt-1.5 max-h-[258px] overflow-y-auto pr-1 scrollbar-thin">
              {equipmentList.map((eq) => {
                const isOnline = eq.status === "ONLINE";
                const isWarning = eq.status === "WARNING";
                const isOffline = eq.status === "OFFLINE";
                
                return (
                  <div 
                    key={eq.id}
                    className={`border rounded-xl p-3 flex flex-col justify-between transition-all duration-300 ${
                      isOnline 
                        ? "bg-brand-success/5 border-brand-success/15 hover:border-brand-success/35" 
                        : isWarning 
                        ? "bg-brand-warning/5 border-brand-warning/15 hover:border-brand-warning/35 animate-pulse" 
                        : "bg-[#07070a]/40 border-brand-primary/10 opacity-70 hover:opacity-90"
                    }`}
                  >
                    <div className="flex items-start justify-between text-left">
                      <div>
                        <div className="flex items-center gap-1.5">
                          <span className={`h-1.5 w-1.5 rounded-full ${isOnline ? "bg-brand-success animate-ping" : isWarning ? "bg-brand-warning" : "bg-brand-text-secondary"}`} />
                          <span className="text-[10px] font-bold uppercase text-brand-text-primary tracking-wider font-heading">{eq.name}</span>
                        </div>
                        <span className="text-[8px] text-brand-text-secondary uppercase tracking-widest font-mono mt-0.5 block">{eq.id} • {eq.type}</span>
                      </div>
                      
                      <button
                        onClick={() => handleToggleEquipment(eq.id, eq.name)}
                        className={`w-8 h-4 rounded-full p-0.5 transition-colors duration-300 relative cursor-pointer outline-none flex items-center ${
                          isOffline ? "bg-brand-border" : "bg-brand-primary"
                        }`}
                        title={isOffline ? "Switch ON" : "Switch OFF"}
                      >
                        <div 
                          className={`w-3 h-3 rounded-full bg-[#0d0f14] shadow-md transform transition-transform duration-300 ${
                            isOffline ? "translate-x-0" : "translate-x-4"
                          }`}
                        />
                      </button>
                    </div>

                    <div className="mt-2.5 flex items-center justify-between text-[8px] border-t border-brand-primary/5 pt-1.5">
                      <div className="flex flex-col text-left">
                        <span className="text-[7px] text-brand-text-secondary">LOCATION</span>
                        <span className="text-brand-text-primary font-bold">{eq.plant}</span>
                      </div>
                      <div className="flex flex-col text-right">
                        <span className="text-[7px] text-brand-text-secondary">LOAD COE</span>
                        <span className={`font-bold ${isOffline ? "text-brand-text-secondary" : isWarning ? "text-brand-warning" : "text-brand-primary"}`}>{eq.load}%</span>
                      </div>
                    </div>
                  </div>
                );
              })}
            </div>
          </CyberCard>
        </div>

      </div>

      {/* 3. SYSTEM LOGS & DOCUMENTS ROW */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6" id="scada">
        
        {/* Recent Ingested Documents */}
        <CyberCard 
          title="Recent Ingested Documents" 
          subtitle="Latest manuals and technical files registered in database"
        >
          <div className="w-full h-44 bg-brand-bg/50 border border-brand-primary/10 rounded-xl p-4 flex flex-col font-mono text-[10px] leading-relaxed overflow-hidden relative">
            <div className="flex-1 overflow-y-auto pr-1 space-y-2 text-left scrollbar-thin">
              {stats && stats.recentUploads && stats.recentUploads.length > 0 ? (
                stats.recentUploads.map((doc: any, idx: number) => (
                  <div key={doc._id || idx} className="flex items-center justify-between text-brand-text-secondary/95 border-b border-brand-primary/5 pb-1">
                    <div className="flex items-center space-x-2">
                      <span className="px-1 py-0.25 rounded text-[7px] font-extrabold shrink-0 border select-none bg-brand-primary/10 border-brand-primary/20 text-brand-primary">
                        {doc.format ? doc.format.toUpperCase() : "TXT"}
                      </span>
                      <span className="break-all sm:break-normal text-brand-text-primary max-w-[150px] md:max-w-[200px] truncate" title={doc.filename}>
                        {doc.filename}
                      </span>
                      <span className="text-[7.5px] text-brand-text-secondary">
                        ({doc.chunksCount || 0} chunks)
                      </span>
                    </div>
                    <div className="flex items-center space-x-2 shrink-0">
                      <span className={`text-[7.5px] uppercase font-bold ${
                        doc.status === "OCR_DONE" ? "text-brand-success" : "text-brand-warning animate-pulse"
                      }`}>
                        {doc.status || "OCR_DONE"}
                      </span>
                      <span className="text-[8px] text-brand-text-secondary">
                        {new Date(doc.createdAt).toLocaleTimeString()}
                      </span>
                    </div>
                  </div>
                ))
              ) : (
                <div className="text-brand-text-secondary/60 text-center py-10">
                  No recently uploaded documents found.
                </div>
              )}
            </div>
          </div>
        </CyberCard>

        {/* SCADA Operations Terminal Logs */}
        <CyberCard 
          title="SCADA Operations Terminal Logs" 
          subtitle="Real-time security checks and monitoring feeds"
        >
          <div className="w-full h-44 bg-brand-bg/50 border border-brand-primary/10 rounded-xl p-4 flex flex-col font-mono text-[10px] leading-relaxed overflow-hidden relative">
            <div 
              ref={scadaContainerRef}
              className="flex-1 overflow-y-auto pr-1 space-y-2 text-left scrollbar-thin"
            >
              {scadaLogs.map((log) => (
                <div key={log.id} className="flex items-start space-x-2 text-brand-text-secondary/95">
                  <span className={`px-1 py-0.25 rounded text-[7px] font-extrabold shrink-0 border select-none ${
                    log.status === "warning" 
                      ? "bg-brand-warning/10 border-brand-warning/20 text-brand-warning" 
                      : log.status === "error" 
                      ? "bg-brand-danger/10 border-brand-danger/20 text-brand-danger animate-pulse" 
                      : log.status === "info" 
                      ? "bg-brand-secondary/10 border-brand-secondary/20 text-brand-secondary" 
                      : "bg-brand-success/10 border-brand-success/20 text-brand-success"
                  }`}>
                    {log.prefix}
                  </span>
                  <span className="break-all sm:break-normal">{log.text}</span>
                </div>
              ))}
            </div>
          </div>
        </CyberCard>

      </div>

      {/* SVG Gradient definition wrapper */}
      <svg className="hidden">
        <defs>
          <linearGradient id="areaGrad" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#06B6D4" stopOpacity="0.15" />
            <stop offset="100%" stopColor="#06B6D4" stopOpacity="0" />
          </linearGradient>
        </defs>
      </svg>

    </div>
  );
}
