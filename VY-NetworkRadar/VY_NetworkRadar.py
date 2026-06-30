import socket
import psutil
import ipaddress
import customtkinter as ctk

# --- AĞ KEŞİF MODÜLÜ (Zero-Telemetry) ---
def get_local_network_info() -> dict:
    """
    Sıfır telemetri prensibiyle yerel makinenin IP adresini ve Subnet Maskesini tespit eder.
    """
    network_info = {"ip": "-", "netmask": "-", "cidr_network": "-"}
    
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("10.255.255.255", 1))
            local_ip = s.getsockname()[0]
            network_info["ip"] = local_ip
    except Exception:
        return network_info

    try:
        interfaces = psutil.net_if_addrs()
        for interface_name, interface_addresses in interfaces.items():
            for address in interface_addresses:
                if address.family == socket.AF_INET and address.address == local_ip:
                    network_info["netmask"] = address.netmask
                    if network_info["netmask"]:
                        network_str = f"{local_ip}/{network_info['netmask']}"
                        network_obj = ipaddress.IPv4Network(network_str, strict=False)
                        network_info["cidr_network"] = str(network_obj)
                    return network_info
    except Exception:
        pass
        
    return network_info

# --- ARAYÜZ (GUI) TASARIMI ---
class VYNetworkRadarApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Temel Pencere Ayarları
        self.title("VY Network Radar - DevSecOps Edition")
        self.geometry("600x400")
        self.resizable(False, False)
        
        # Tema Ayarları (Karanlık Tema - Gizlilik Odaklı Tasarım)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Başlık Etiketi
        self.title_label = ctk.CTkLabel(self, text="📡 VY Network Radar", font=ctk.CTkFont(size=24, weight="bold"))
        self.title_label.pack(pady=(20, 10))

        self.subtitle_label = ctk.CTkLabel(self, text="Zero-Telemetry Local Network Discovery Tool", font=ctk.CTkFont(size=12), text_color="gray")
        self.subtitle_label.pack(pady=(0, 20))

        # Bilgi Çerçevesi (Frame)
        self.info_frame = ctk.CTkFrame(self, width=500, height=150)
        self.info_frame.pack(pady=10, padx=20, fill="both", expand=True)

        # Bilgi Etiketleri (Grid Düzeni)
        self.ip_label_title = ctk.CTkLabel(self.info_frame, text="Yerel IP Adresi:", font=ctk.CTkFont(weight="bold"))
        self.ip_label_title.grid(row=0, column=0, padx=20, pady=15, sticky="w")
        self.ip_value = ctk.CTkLabel(self.info_frame, text="Bekleniyor...")
        self.ip_value.grid(row=0, column=1, padx=20, pady=15, sticky="w")

        self.mask_label_title = ctk.CTkLabel(self.info_frame, text="Subnet Mask:", font=ctk.CTkFont(weight="bold"))
        self.mask_label_title.grid(row=1, column=0, padx=20, pady=15, sticky="w")
        self.mask_value = ctk.CTkLabel(self.info_frame, text="Bekleniyor...")
        self.mask_value.grid(row=1, column=1, padx=20, pady=15, sticky="w")

        self.cidr_label_title = ctk.CTkLabel(self.info_frame, text="Hedef Ağ (CIDR):", font=ctk.CTkFont(weight="bold"))
        self.cidr_label_title.grid(row=2, column=0, padx=20, pady=15, sticky="w")
        self.cidr_value = ctk.CTkLabel(self.info_frame, text="Bekleniyor...")
        self.cidr_value.grid(row=2, column=1, padx=20, pady=15, sticky="w")

        # İşlem Butonu
        self.scan_button = ctk.CTkButton(self, text="Sistem Ağ Bilgilerini Al", command=self.update_network_info, font=ctk.CTkFont(weight="bold"))
        self.scan_button.pack(pady=20)

    def update_network_info(self):
        """Butona tıklandığında ağ bilgilerini alır ve arayüzü günceller."""
        self.scan_button.configure(state="disabled", text="Taranıyor...")
        
        info = get_local_network_info()
        
        # Arayüzü güncellerken ufak bir gecikme hissi vermesi için (opsiyonel)
        self.after(500, self._apply_updates, info)

    def _apply_updates(self, info):
        self.ip_value.configure(text=info.get("ip") if info.get("ip") else "Bulunamadı")
        self.mask_value.configure(text=info.get("netmask") if info.get("netmask") else "Bulunamadı")
        self.cidr_value.configure(text=info.get("cidr_network") if info.get("cidr_network") else "Bulunamadı", text_color="#00FF00")
        
        self.scan_button.configure(state="normal", text="Bilgileri Güncelle")

if __name__ == "__main__":
    app = VYNetworkRadarApp()
    app.mainloop()