"use client";

import React, { useState } from "react";
import { 
  ShieldCheck, AlertOctagon, Wrench, Sparkles, Activity, FileText 
} from "lucide-react";
import CyberCard from "@/components/ui/CyberCard";

interface MaintenanceAlert {
  id: string;
  equipmentId: string;
  equipmentName: string;
  severity: "HIGH" | "MEDIUM" | "LOW";
  description: string;
  timestamp: string;
  rca: string;
  recommendation: string;
}

export default function CompliancePage() {
  const [selectedAlertId, setSelectedAlertId] = useState<string>("ALT-092");

  const [safetyChecklist, setSafetyChecklist] = useState({
    sslHandshake: true,
    neo4jHealth: true,
    astmCompliance: true,
    scadaTunnel: false,
  });

  const [alerts] = useState<MaintenanceAlert[]>([
    {
      id: "ALT-092",
      equipmentId: "EQ-102",
      equipmentName: "Zone B Heat Exchanger",
      severity: "HIGH",
      description: "Thermal dilation spike: coolant inlet restriction detected.",
      timestamp: "10:14:02",
      rca: "Degraded thermal efficiency due to scaling on outer shell surfaces, compounding with a temporary sensor calibration drift.",
      recommendation: "Execute visual inspection of the tube shell, flush primary coolant channels with chemical scale remover, and recalibrate coolant pressure transducers."
    },
    {
      id: "ALT-088",
      equipmentId: "EQ-101",
      equipmentName: "Compressor C",
      severity: "MEDIUM",
      description: "Vibration threshold anomaly in primary motor bearings.",
      timestamp: "09:45:11",
      rca: "Lube oil viscosity degradation coupled with slight rotor misalignment on the primary coupling shaft.",
      recommendation: "Sample lubricating oil to check for particulate metal contaminants, adjust coupling alignment tolerances, and schedule bearing lubrication flush within 24 operational hours."
    },
    {
      id: "ALT-085",
      equipmentId: "EQ-104",
      equipmentName: "Turbine Generator A",
      severity: "LOW",
      description: "Sub-optimal combustion exhaust gas temperature balance.",
      timestamp: "08:12:35",
      rca: "Minor nozzle clogging inside burner nozzle sector 4 resulting in fuel injection pressure variance.",
      recommendation: "Monitor exhaust gas differentials. Schedule turbine exhaust check during next planned outage and clean nozzle tips."
    }
  ]);

  const checkedCount = Object.values(safetyChecklist).filter(Boolean).length;
  const complianceLevel = Number(((checkedCount / 4) * 100).toFixed(2));
  const selectedAlert = alerts.find(a => a.id === selectedAlertId);

  return (
    <div className="flex flex-col gap-6 select-none font-mono">
      
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        
        {/* LEFT COLUMN: Compliance dials & safety checklists (col-span-4) */}
        <div className="lg:col-span-5 flex flex-col">
          <CyberCard 
            title="ASTM / OISD Safety Compliance" 
            subtitle="Concentric compliance parameters & safety checks"
          >
            <div className="flex flex-col items-center justify-center p-6 bg-[#07070a]/30 border border-brand-primary/10 rounded-xl relative mt-1 min-h-[360px]">
              
              {/* Radial Dial Gauge */}
              <div className="relative w-32 h-32 flex items-center justify-center mt-2">
                <div className="absolute inset-0 rounded-full bg-brand-success/5 blur-lg" />
                <svg className="absolute w-full h-full" viewBox="0 0 100 100">
                  <circle cx="50" cy="50" r="42" className="stroke-brand-primary/10 fill-none stroke-[2.5]" />
                  <circle 
                    cx="50" 
                    cy="50" 
                    r="42" 
                    className="stroke-brand-success fill-none stroke-[2.5] transition-all duration-500" 
                    strokeDasharray="264"
                    style={{
                      strokeDashoffset: 264 - (264 * complianceLevel) / 100,
                      transform: "rotate(-90deg)",
                      transformOrigin: "50px 50px",
                    }}
                  />
                  <circle cx="50" cy="50" r="34" className="stroke-brand-primary/10 fill-none stroke-1 animate-pulse" strokeDasharray="3 3" />
                </svg>
                <div className="flex flex-col items-center z-10 select-none">
                  <span className="font-heading text-lg font-extrabold text-brand-success tracking-tight transition-all duration-300">
                    {complianceLevel}%
                  </span>
                  <span className="text-[7.5px] text-brand-text-secondary tracking-widest font-mono uppercase mt-0.5">
                    OISD_INDEX
                  </span>
                </div>
              </div>

              {/* Safety Checklist Toggle controls */}
              <div className="w-full flex flex-col gap-3 mt-6 text-xs text-left border-t border-brand-primary/10 pt-4">
                <label className="flex items-center space-x-3 cursor-pointer group select-none">
                  <input
                    type="checkbox"
                    checked={safetyChecklist.sslHandshake}
                    onChange={(e) => setSafetyChecklist(prev => ({ ...prev, sslHandshake: e.target.checked }))}
                    className="rounded border-brand-primary/20 text-brand-primary focus:ring-0 focus:ring-offset-0 bg-[#0d0f14] h-3.5 w-3.5 cursor-pointer accent-brand-primary"
                  />
                  <span className="group-hover:text-brand-text-primary transition-colors">SSL_TUNNEL_COMMUNICATIONS_ACTIVE</span>
                </label>
                
                <label className="flex items-center space-x-3 cursor-pointer group select-none">
                  <input
                    type="checkbox"
                    checked={safetyChecklist.neo4jHealth}
                    onChange={(e) => setSafetyChecklist(prev => ({ ...prev, neo4jHealth: e.target.checked }))}
                    className="rounded border-brand-primary/20 text-brand-primary focus:ring-0 focus:ring-offset-0 bg-[#0d0f14] h-3.5 w-3.5 cursor-pointer accent-brand-primary"
                  />
                  <span className="group-hover:text-brand-text-primary transition-colors">NEO4J_GRAPH_RELATIONS_VERIFIED</span>
                </label>
                
                <label className="flex items-center space-x-3 cursor-pointer group select-none">
                  <input
                    type="checkbox"
                    checked={safetyChecklist.astmCompliance}
                    onChange={(e) => setSafetyChecklist(prev => ({ ...prev, astmCompliance: e.target.checked }))}
                    className="rounded border-brand-primary/20 text-brand-primary focus:ring-0 focus:ring-offset-0 bg-[#0d0f14] h-3.5 w-3.5 cursor-pointer accent-brand-primary"
                  />
                  <span className="group-hover:text-brand-text-primary transition-colors">ASTM_OISD_STANDARD_VALIDATOR_ON</span>
                </label>
                
                <label className="flex items-center space-x-3 cursor-pointer group select-none">
                  <input
                    type="checkbox"
                    checked={safetyChecklist.scadaTunnel}
                    onChange={(e) => setSafetyChecklist(prev => ({ ...prev, scadaTunnel: e.target.checked }))}
                    className="rounded border-brand-primary/20 text-brand-primary focus:ring-0 focus:ring-offset-0 bg-[#0d0f14] h-3.5 w-3.5 cursor-pointer accent-brand-primary"
                  />
                  <span className="group-hover:text-brand-text-primary transition-colors">SCADA_FIREWALL_COMMUNICATION_SHIELD</span>
                </label>
              </div>

            </div>
          </CyberCard>
        </div>

        {/* RIGHT COLUMN: Maintenance Incident Alerts & Diagnostics (col-span-8) */}
        <div className="lg:col-span-7 flex flex-col gap-6">
          <CyberCard 
            title="Maintenance Incident Alarms & AI Diagnostics" 
            subtitle="Real-time machinery incident logs & root cause analysis suggestions"
          >
            <div className="grid grid-cols-1 md:grid-cols-12 gap-5 mt-1.5 text-left">
              
              {/* Incidents logs list (col-span-5) */}
              <div className="md:col-span-5 flex flex-col gap-2 max-h-[360px] overflow-y-auto pr-1 scrollbar-thin">
                <span className="text-[8px] text-brand-text-secondary uppercase tracking-wider font-bold mb-1 select-none">ACTIVE ALERTS LOGS</span>
                
                {alerts.map((alert) => {
                  const isHigh = alert.severity === "HIGH";
                  const isMedium = alert.severity === "MEDIUM";
                  const isSelected = alert.id === selectedAlertId;

                  return (
                    <div 
                      key={alert.id}
                      onClick={() => setSelectedAlertId(alert.id)}
                      className={`border rounded-xl p-3.5 cursor-pointer text-left transition-all duration-300 relative ${
                        isSelected 
                          ? "bg-brand-primary/10 border-brand-primary shadow-[0_0_12px_rgba(6,182,212,0.05)]" 
                          : "bg-[#07070a]/40 border-brand-primary/5 hover:border-brand-primary/20"
                      }`}
                    >
                      <div className="flex items-center justify-between gap-1.5">
                        <div className="flex items-center gap-1.5 min-w-0">
                          <AlertOctagon className={`h-4.5 w-4.5 shrink-0 ${isHigh ? "text-brand-danger animate-pulse" : isMedium ? "text-brand-warning" : "text-brand-primary"}`} />
                          <span className="text-[10px] font-bold text-brand-text-primary uppercase truncate font-heading">{alert.equipmentName}</span>
                        </div>
                        <span className={`text-[7px] font-extrabold px-1.5 py-0.25 rounded border shrink-0 select-none ${
                          isHigh 
                            ? "bg-brand-danger/10 border-brand-danger/25 text-brand-danger" 
                            : isMedium 
                            ? "bg-brand-warning/10 border-brand-warning/25 text-brand-warning" 
                            : "bg-brand-primary/10 border-brand-primary/25 text-brand-primary"
                        }`}>
                          {alert.severity}
                        </span>
                      </div>
                      <p className="text-[9px] text-brand-text-secondary line-clamp-2 mt-2 leading-relaxed">{alert.description}</p>
                      <div className="text-[7.5px] text-brand-text-secondary mt-2 border-t border-brand-primary/5 pt-1.5 flex justify-between select-none">
                        <span>ALERT: {alert.id}</span>
                        <span>TS: {alert.timestamp}</span>
                      </div>
                    </div>
                  );
                })}
              </div>

              {/* Dynamic Diagnostics RCA details (col-span-7) */}
              <div className="md:col-span-7 flex flex-col">
                <span className="text-[8px] text-brand-text-secondary uppercase tracking-wider font-bold mb-1 select-none">AI CORE DIAGNOSTICS & RCA</span>
                {selectedAlert ? (
                  <div className="bg-[#0d0f14]/85 border border-brand-primary/10 rounded-xl p-4 flex flex-col gap-4 flex-1 min-h-[280px]">
                    <div className="flex items-center justify-between border-b border-brand-primary/10 pb-2.5">
                      <div className="flex items-center gap-1.5">
                        <Wrench className="h-4.5 w-4.5 text-brand-primary" />
                        <span className="text-[9.5px] font-bold text-brand-text-primary uppercase font-heading">{selectedAlert.equipmentName}</span>
                      </div>
                      <span className="text-[8px] text-brand-text-secondary font-mono tracking-widest uppercase select-all bg-brand-primary/5 border border-brand-primary/10 px-2 py-0.5 rounded font-bold">
                        {selectedAlert.id}
                      </span>
                    </div>

                    <div className="text-[10px]">
                      <span className="text-brand-text-secondary uppercase font-extrabold tracking-wider block mb-1">Root Cause Analysis (RCA)</span>
                      <p className="text-brand-text-primary leading-relaxed font-sans text-xs pl-2 border-l border-brand-warning/50">
                        {selectedAlert.rca}
                      </p>
                    </div>

                    <div className="text-[10px] mt-2">
                      <span className="text-brand-success uppercase font-extrabold tracking-wider flex items-center gap-1.5 mb-1">
                        <Sparkles className="h-4.5 w-4.5 text-brand-success" />
                        AI Maintenance Recommendation
                      </span>
                      <p className="text-brand-text-primary leading-relaxed font-sans text-xs pl-2 border-l border-brand-success/50">
                        {selectedAlert.recommendation}
                      </p>
                    </div>

                    <div className="mt-auto border-t border-brand-primary/5 pt-3.5 flex items-center justify-between text-[9px] text-brand-text-secondary select-none">
                      <div className="flex items-center gap-1">
                        <Activity className="h-3.5 w-3.5 text-brand-primary" />
                        <span>INTEGRATION: ACTIVE</span>
                      </div>
                      <span className="text-[7.5px] uppercase font-bold tracking-widest bg-brand-primary/5 px-2 py-0.5 rounded border border-brand-primary/10">
                        METRICS HEALTH MONITOR
                      </span>
                    </div>
                  </div>
                ) : (
                  <div className="border border-brand-primary/10 rounded-xl bg-[#0d0f14]/50 flex items-center justify-center p-8 flex-1 min-h-[280px]">
                    <span className="text-[10px] text-brand-text-secondary/50 font-mono text-center">Select an incident alarm log on the left to run cognitive analytics</span>
                  </div>
                )}
              </div>

            </div>
          </CyberCard>
        </div>

      </div>

    </div>
  );
}
